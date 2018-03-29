import re


class RegexProjectGenerator(object):
    def __init__(self, types):
        self._types = types

    def regex(self):
        regex = []
        for type in self._types:
            if type == 'python':
                regex.append('(.*\.py)')
            if type == 'go':
                regex.append('(.*\.go)')
        return regex
