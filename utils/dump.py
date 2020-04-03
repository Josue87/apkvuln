def write_results(f, vulnerabilities):
    print(f"[*] vulnerabilities found in {f}")
    for vuln in vulnerabilities:
        name = "./results/" + f.replace("/", ".").replace(".java", "") + ".txt"
        with open(name, "w") as dump_result:
            dump_result.write(f + "\n")
            dump_result.write("-"*len(f) + "\n")
            try:
                for k,v in vuln.items():
                    dump_result.write(f"{k}: {v}\n")
                dump_result.write("\n")
            except:
                pass