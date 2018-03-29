from mamba import description, context, it
from expects import expect, equal

import regex_project_type
import constants


with description('Regex Project Generator'):
    with context('regex for python'):
        with it('returns it'):
            python_project = regex_project_type.RegexProjectGenerator(['python'])

            expect(python_project.regex()).to(equal([constants.PYTHON_REGEX]))

    with context('having several project types'):
        with it('returns a list'):
            several_projects = regex_project_type.RegexProjectGenerator(['python','go'])

            expect(several_projects.regex()).to(equal([constants.PYTHON_REGEX, constants.GO_REGEX]))
