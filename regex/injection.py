from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r".*eval\(([^\"\' ]+)|(.+[+].+)\)\s*;", r".*exec\(([^\"\' ]+)|(.+[+].+)\)\s*;",
                        r".*system\(([^\"\' ]+)|(.+[+].+)\)\s*;", r".+.command\([^\"\'\n]+\)\s*;",
                        r".+.(command|executeCommand)\([^\"\'\n]+\)\s*;"]
        super(Regex, self).__init__(pattern_list, "injection")