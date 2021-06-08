from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r".*DebuggingEnabled\(true\)"]
        file_type = ["java"]
        super(Regex, self).__init__(pattern_list, "debug enabled", file_type)