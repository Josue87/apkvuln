from abc import ABC
from utils.check_code import analysis


class Template(ABC):

    def __init__(self, patterns, vulnerability, file_type, description=""):
        self.patterns = patterns
        self.vulnerability = vulnerability
        self.description = description
        self.file_type = file_type

    def check_code(self, filename, code):
        result = None
        try:
            if filename.split(".")[-1] in self.file_type:
                result = analysis(self.patterns, filename, code, 
                        self.vulnerability, self.description)
        except:
            pass
        return result