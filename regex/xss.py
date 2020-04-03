from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r".*write\(([^\"\'\n]+)|(.+[+].+)\)\s*;"]
        super(Regex, self).__init__(pattern_list, "xss")
