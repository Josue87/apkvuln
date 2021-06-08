from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r".*\.getInstance\((\'|\")?(md5|sha1)(\'|\")?\)", r".+(init|initialize)\(\d{1,3}\);"]
        file_type = ["java"]
        super(Regex, self).__init__(pattern_list, "insecure cipher", file_type)