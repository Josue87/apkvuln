from regex._template import Template

class Regex(Template):

    def __init__(self):
        pattern_list = [r".*\.putString\([\'\"]?(user|pass|api[-\_]*key|token|secret|credential).+\)",
                        r".*createTempFile\(.*\)[^\}]*(credential|pass|user|api)",
                        r".*getExternalStorageDirectory\(\)[^\}]*(credential|pass|user|api)"]
        file_type = ["java"]
        super(Regex, self).__init__(pattern_list, "insecure storage", file_type)