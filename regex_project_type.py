import re

import constants


class RegexProjectGenerator(object):
    def __init__(self, types):
        self._types = types

    def regex(self):
        regex = []
        for type in self._types:
            if type == 'python':
                regex.append(constants.PYTHON_REGEX)
            if type == 'go':
                regex.append(constants.GO_REGEX)
        return regex
