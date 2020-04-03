from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r".+(init|initialize)\(\d{1,3}\);"]
        super(Regex, self).__init__(pattern_list, "week crypto key")
