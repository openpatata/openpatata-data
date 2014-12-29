
"""Check our data for syntax errors and compliance with the schema. This
script takes one argument, which is the path to a folder in which
items of a particular schema reside.
"""

from pathlib import Path
import sys

from jsonschema import (
    Draft4Validator as Validator,
    FormatChecker)
import yaml


def main(folder):
    # The shell exit status. Travis will report a "build" fail for 0
    # and success for 1. We set to 1 if any item is not valid.
    exit_status = 0

    with (Path('_schemas')/'{filename}.yaml'.format(
            filename=folder.rstrip('s/'))).open() as f:
        validator = Validator(yaml.load(f), format_checker=FormatChecker(
            ['date']))

    for item in Path(folder).iterdir():
        with item.open() as f:
            errors = list(validator.iter_errors(yaml.load(f)))
            if errors:
                exit_status = 1
                for error in errors:
                    print('{item}: [{field}] {message}'.format(
                        item=item, field='/'.join(map(str, error.path)),
                        message=error.message))

    return exit_status


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
