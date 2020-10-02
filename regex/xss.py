from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r"[\W]write\(([^,\"\'\n]+)\)", r'setJavaScriptEnabled(true)']
        super(Regex, self).__init__(pattern_list, "xss")
