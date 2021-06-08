from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r"((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"]
        file_type = ["xml", "html", "js", "java", "json"]
        super(Regex, self).__init__(pattern_list, "ip", file_type)