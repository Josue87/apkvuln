from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r".+\.loadUrl\([^\'\"\n]+\)",
                         r".+\.loadUrl\([\'\"]javascript\:.*[\'\"]\s?\+\s?.+\s?\)",
                         r".+\.addJavascriptInterface\(.+\)"]
        file_type = ["java"]
        super(Regex, self).__init__(pattern_list, "xss", file_type)