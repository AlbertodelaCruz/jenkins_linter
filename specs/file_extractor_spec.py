from mamba import description, context, it
from expects import expect, equal

import file_extractor
import regex_project_type


with description('File Extractor'):
    with context('for a python project'):
        with context('given a list of files'):
            with it('gets the python files'):
                python_regex = regex_project_type.RegexProjectGenerator(['python']).regex()[0]
                test_file_list = ['foo.py', 'foo.txt']
                _file_extractor = file_extractor.FileExtractorFromRegex(python_regex)

                result = _file_extractor.process(test_file_list)

                expect(result).to(equal(['foo.py']))
