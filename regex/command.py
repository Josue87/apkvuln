from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r".*[^\w](eval|exec|system|command)\([a-zA-Z]+[^\"\' \n]*\)"]
        file_type = ["js", "java"]
        super(Regex, self).__init__(pattern_list, "system command", file_type)