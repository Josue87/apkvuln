from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r".+['\"]select\s.+\sfrom\s.+[\'\"]\s?\+\s?.+\)?"]
        file_type = ["java"]
        super(Regex, self).__init__(pattern_list, "sqli", file_type)