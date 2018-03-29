import re
import regex_project_type


class FileExtractorFromRegex(object):
    def __init__(self, regex):
        self._regex = regex

    def process(self, file_list):
        matches = []
        for file in file_list:
            regex_match = re.match(self._regex, file)
            if regex_match:
                matches.append(regex_match.group(0))
        return matches
