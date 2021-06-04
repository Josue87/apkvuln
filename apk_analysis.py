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

def get_java_files(directory):
    # Returns all files inside the apk-work/<directory> folder
    result = Popen(["find",  directory, "-type", "f", "-name", "*"], stdout=PIPE, stderr=PIPE)
    try:
        return remove_empty_result(result.stdout.read().decode(errors="ignore").split("\n"))
    except:
        return []

def start_analysis(directory, apk_name):
    # Scans files one by one
    files = get_java_files(directory)
    modules = get_all_modules()
    # creating results folder for the apk
    results_folder_name = f"results/{apk_name}"
    results_folder = Path(results_folder_name)
    results_folder.mkdir(parents=True, exist_ok=True)
    for f in files:
        vulns = []
        try:
            with open(f, "r") as open_file:
                file_data = open_file.read()
                if file_data:
                    for m in modules:
                        data = m.check_code(f, file_data)
                        if data:
                            vulns.extend(data)
                            
                    if vulns:
                        write_results(f.replace("apk-work/", ""), vulns, results_folder_name)
        except KeyboardInterrupt as e:
           raise e
        except:
            pass

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
    print_info("Starting analysis...")
    start_analysis(folder, apk_name)
    print_ok(f"Done! Check the results/{apk_name} folder...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_info("\nCtrl^C - End.")
    except Exception as e:
        print_error("[-] Something has gone wrong")
        print_error(e)
