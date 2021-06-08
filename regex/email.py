from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r"[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9]+[-]*[a-zA-Z0-9]+\.[a-zA-Z0-9-]{2,}"]
        file_type = ["xml", "html", "js", "java", "json"]
        super(Regex, self).__init__(pattern_list, "emails", file_type)