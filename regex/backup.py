from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r".*allowBackup\([\w]+\)\=\(.+\)0xffffffff"]
        file_type = ["xml"]
        super(Regex, self).__init__(pattern_list, "backup", file_type)