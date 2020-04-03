from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r".+[\"']select.+from.+\([\"'][^?\n]+[\"']\)[\"'][^\n]+", r".+select.+from.+ [+] .+"]
        super(Regex, self).__init__(pattern_list, "sqli")