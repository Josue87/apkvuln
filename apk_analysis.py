from subprocess import check_call, PIPE, Popen
import argparse
from os import system, walk, path
from sys import exit
from threading import Thread
import importlib
from utils.dump import write_results
from utils.banner import banner


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
    # Get .java files and move the folder to apk-work folder
    system(f"apkx {apk} 2> /dev/null")
    system(f"mv {apk.replace('.apk','')} apk-work")

def remove_empty_result(files):
    # Sometimes the result has "" in the list
    while "" in files:
        files.remove("")
    return files

def get_java_files(directory):
    # Returns all .java files inside the apk-work/<directory> folder
    result = Popen(["find",  directory, "-name", "*.java"], stdout=PIPE, stderr=PIPE)
    return remove_empty_result(result.stdout.read().decode(errors="ignore").split("\n"))

def start_analysis(directory):
    # Scans files one by one
    files = get_java_files(directory)
    modules = get_all_modules()
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
                        write_results(f, vulns)
        except Exception as e:
            print("[-] " + str(e))

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
        print("Install apkx: https://github.com/b-mueller/apkx")
        exit(1)
    apk = args.apk
    th = Thread(target=execute_apkx, args=(apk,))
    print("[*] Working in decompile, be patience this process may take a few minutes...")
    th.start()
    th.join()
    print("[+] Done!")
    folder = "apk-work/" + apk.replace(".apk", "")
    print("Starting analysis...")
    start_analysis(folder)
    print("[+] The analysis is finished, check the results folder...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[*] Ctrl^C - End.")
    except Exception as e:
        print("[-] Something has gone wrong")
        print(e)
