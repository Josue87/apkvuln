import re


def analysis(patterns_list, file_name, code, vulnerability, description):
    data = []
    line=[]
    for m in re.finditer('.*\n', code):
        line.append(m.end()+1)
    for pattern in patterns_list:
        match = re.compile(pattern, re.MULTILINE|re.IGNORECASE) 
                
        for m in re.finditer(match, code):
            file_line = next(i for i in range(len(line)) if line[i] > m.start())
            match_pat = m.group(0)
            if len(match_pat.split("\n")) < 60:
                data.append({"file": file_name, "line": file_line, 
                        "vulnerability": vulnerability, "code": match_pat.strip(),
                        "description": description})
    return data