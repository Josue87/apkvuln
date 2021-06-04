from utils.curstom_print import print_info


def write_results(code_file, vulnerabilities, results_folder_name):
    print_info(f"vulnerabilities found in {code_file}")
    for vuln in vulnerabilities:
        name = results_folder_name + "/" + code_file.replace("/", ".") + ".txt"
        with open(name, "w") as dump_result:
            dump_result.write(code_file + "\n")
            dump_result.write("-"*len(code_file) + "\n")
            try:
                for k,v in vuln.items():
                    dump_result.write(f"{k}: {v}\n")
                dump_result.write("\n")
            except:
                pass