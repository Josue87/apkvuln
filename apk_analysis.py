from subprocess import check_call, PIPE, Popen
import argparse
from os import system, walk, path
from pathlib import Path
from sys import exit
from threading import Thread
import importlib
from utils.dump import write_results
from utils.banner import banner
from utils.curstom_print import print_info, print_error, print_ok
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime



def get_args():
    # Arguments for the tool
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--apk", help="Apk file",required=True)
    return parser.parse_args()

def check_apkx():
    # Verify if apkx is install in the system
    try:
        check_call(["apkx", "-h" ], stdout=PIPE, stderr=PIPE)
        apkx = True
    except:
        apkx = False
    return apkx

def execute_apkx(apk):
    # Get files and move the folder to apk-work folder
    work_folder = Path("apk-work")
    work_folder.mkdir(parents=True, exist_ok=True)
    system(f"cp {apk} apk-work/{apk}")
    system(f"cd apk-work && apkx {apk} 2> /dev/null")
    # Delete aux files
    system(f"cd apk-work && rm {apk} 2> /dev/null")
    system(f"cd apk-work && rm *.zip 2> /dev/null")

def remove_empty_result(files):
    # Sometimes the result has "" in the list
    while "" in files:
        files.remove("")
    return files

def get_code_files(directory):
    # Returns all 'code' files inside the apk-work/<apkfolder> folder
    type_file_to_search = ["js", "xml", "html", "java", "json", "kt", "kts"]
    # TODO: review this list
    folders_to_check = ["src/android", "src/kotlin", "src/javax", "src/okhttp3",
                        "assets/www/cordova-js-src", "assets/www/plugins"]
    first = True
    command = "egrep -v "
    for aux in folders_to_check:
        if first:
            command += aux
            first = False
        else:
            command += f"|{aux}"
    command = command[0:-1]
    total_files = []
    for ftype in type_file_to_search:
        try:
            result = Popen(["find",  directory, "-type", "f", "-name", f"*.{ftype}", "-size", "-10M"], stdout=PIPE, stderr=PIPE)
            
            grep_process = Popen(command.split(" "), stdin=result.stdout, stdout=PIPE)
            result.stdout.close()
            output = grep_process.communicate()[0] 
            total_files.extend(remove_empty_result(output
                                .decode(errors="ignore").split("\n")))
        except:
            pass
    return total_files

def start_check_code(file_name, results_folder_name, modules):
    vulns = []
    # Avoid tests or other files
    folders_to_check = ["test", "bundle.js"]
    for aux in folders_to_check:
        if aux in file_name.lower():
            return
    try:
        open_file = open(file_name, "r")
        file_data = open_file.read()
        open_file.close()
        if file_data:
            with ThreadPoolExecutor(max_workers=2) as executor:
                job = {executor.submit(m.check_code, file_name, file_data): m for m in modules}
                for job_done in as_completed(job):
                    try:
                        data = job_done.result()
                        if data:
                            vulns.extend(data)
                    except:
                        pass
        if vulns:
            write_results(file_name.replace("apk-work/", ""), vulns, results_folder_name)
    except KeyboardInterrupt as e:
        raise e
    except:
        pass

def start_analysis(directory, results_folder_name):
    completed_files = 0
    is25 = False
    is50 = False
    is75 = False
    modules = get_all_modules()
    files = get_code_files(directory)
    total_files = len(files)
    print_info(f"Total code files to be analyzed: {total_files}")
    with ThreadPoolExecutor(max_workers=4) as executor:
        job = {executor.submit(start_check_code, f, results_folder_name, modules): f for f in files}
        for _ in as_completed(job):
            completed_files += 1
            porcentage = completed_files/total_files
            format_float = "{:.2f}%!".format(porcentage*100)
            if porcentage >= 0.75 and not is75:
                print_ok(format_float)
                is75 = True
            elif porcentage >= 0.50 and not is50:
                print_ok(format_float)
                is50 = True
            elif porcentage >= 0.25 and not is25:
                print_ok(format_float)
                is25 = True

def load_module(pwd):
    # Dynamic import
    module = importlib.import_module(pwd.replace("/", "."))
    return module.Regex()

def get_all_modules():
    # Loads all the modules that have the patterns to analyze
    modules = []
    pwd = "regex/"
    for (p, _, files) in walk(pwd):
        modules.extend([load_module(path.join(p, f.replace(".py", ""))) for f in files
                            if ("_" not in f) and (not f.endswith(".pyc"))])
    return modules

def check_v1_signature(apk, apk_name, result_folder):
    try:
        cmd = f"apksigner verify -v {apk}"
        result = Popen(cmd.split(" "), stdout=PIPE, stderr=PIPE)
        content = result.stdout.read().decode()
        signatures = content.split("\n")[1:4]
        data = []
        if "true" in signatures[0]:
            data.append({"file": "signature", "line": 1, 
                        "vulnerability": "signature v1 scheme", "code": signatures[0]})
        if "false" in signatures[2]:
            data.append({"file": "signature", "line": 3, 
                        "vulnerability": "no signature v3 scheme", "code": signatures[2]})      
        if data:               
            write_results("signature", data, result_folder)
    except IndexError:
        print_error("No signature found")
    except:
        print_error("Skipping signature check. You need to install apksigner")

def main():
    print(banner)
    args = get_args()
    if not check_apkx():
        print_error("Install apkx: https://github.com/b-mueller/apkx")
        exit(1)
    apk = args.apk
    apk_name = apk.split('.')[0]
    th = Thread(target=execute_apkx, args=(apk,))
    print_info("Working in decompile, be patience this process may take a few minutes...")
    th.start()
    th.join()
    print_ok("Done!")
    folder = "apk-work/" + apk.replace(".apk", "")
    # Replace AndroidManifest.xml
    try:
        cmd = f"aapt d xmltree {apk} AndroidManifest.xml"
        result = Popen(cmd.split(" "), stdout=PIPE, stderr=PIPE)
        file_data = result.stdout.read().decode()
        with open(f"{folder}/AndroidManifest.xml", "w") as f:
            f.write(file_data)
    except:
        print_error("You need aapt tool to extract AndroidManifest.xml. Skipping")
    # creating results folder for the apk
    now = datetime.now()
    results_folder_name = f"results/{apk_name}/{now.strftime('%Y%m%d-%H:%M')}"
    results_folder = Path(results_folder_name)
    results_folder.mkdir(parents=True, exist_ok=True)
    print_info("Starting analysis...")
    check_v1_signature(apk, apk_name, results_folder_name)
    start_analysis(folder, results_folder_name)
    print_ok(f"Done! Check the {results_folder_name} folder...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_info("\nCtrl^C - Finishing.")
    except Exception as e:
        print_error("[-] Something has gone wrong")
        print_error(e)
