from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r"[^\w]eval\(([^\"\' \n]*)\)", r"[^\w]exec\(([^\"\' \n]*)\)",
                        r"[^\w]system\(([^\"\' \n]*)\)", r"[^\w]command\(([^\"\' \n]*)\)"]
        super(Regex, self).__init__(pattern_list, "injection")