from utils.curstom_print import print_info
from json import dump, load


def write_results(code_file, vulnerabilities, results_folder_name):
    print_info(f"vulnerabilities found in {code_file}")
    name = results_folder_name + "/" + code_file.replace("/", ".") + ".txt"
    name_json = results_folder_name + "/results.json"
    # txt dump
    with open(name, "w") as txt_file:
        txt_file.write(code_file + "\n")
        txt_file.write("-"*len(code_file) + "\n")
        for vuln in vulnerabilities:
            try:
                for k,v in vuln.items():
                    txt_file.write(f"{k}: {v}\n")
                txt_file.write("\n")
            except:
                pass
    # json dump       
    data = {"vulnerabilities": []}
    try:
       json_file = open(name_json, "r+")
       data = load(json_file)
    except:
        json_file = open(name_json, "w")
        
    data["vulnerabilities"].extend(vulnerabilities)
    json_file.seek(0)
    dump(data, json_file)
    json_file.close()