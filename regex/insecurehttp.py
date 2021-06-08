from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r"http:\/\/[^\s\.\n]+\.{1}[^\s\n]+\?{1}[^\n]*(pass|user|token|key)[^\n]*",
                        r".*usesCleartextTraffic\([\w]+\)\=\(.+\)0xffffffff"]
        file_type = ["xml", "html", "js", "java"]
        super(Regex, self).__init__(pattern_list, "insecure http", file_type)