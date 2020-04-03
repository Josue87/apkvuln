from abc import ABC
from utils.check_code import analysis


class Template(ABC):

    def __init__(self, patterns, vulnerability):
        self.patterns = patterns
        self.vulnerability = vulnerability

    def check_code(self, filename, code):
        return analysis(self.patterns, filename, code, self.vulnerability)
