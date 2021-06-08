from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r".*(user(name)?|pass(word)?|api[-\_]*key|secret|credential|clave|account[-]?key)\s?=\s?[\"|\'][^\"\']+[\"|\'].*",
                        r"(pass(word)?|user(name)?).*\.equals\([\'\"].+[\'\"]\)",
                        r".*([\"\']|\/\/).*(api[\s\-\_]?(key)|user[\s\-\_]?(name)?|pass(word)?):.+"]
        file_type = ["xml", "html", "js", "java", "json"]
        super(Regex, self).__init__(pattern_list, "harcoded data", file_type)