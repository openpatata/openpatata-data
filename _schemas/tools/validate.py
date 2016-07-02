
"""Check our data for compliance with the schema.

This script takes one argument, which is the path to a folder containing
items of a particular schema.
"""

from pathlib import Path
import sys

from jsonschema import Draft4Validator as Validator, FormatChecker
import yaml


def _parse_errors(validator, item):
    with item.open() as file:
        # Produce something readable; the default is to print a whote lot
        # of JSON
        return ('{item}:{field}:{message}'
                ''.format(item=item, field='/'.join(map(str, error.path)),
                          message=error.message)
                for error in validator.iter_errors(yaml.load(file)))


def main(folder, schema):
    if not schema:
        schema = ('_schemas', '{}.yaml'.format(folder.rstrip('s/')))
    with Path(*schema).open() as file:
        validator = Validator(yaml.safe_load(file),
                              format_checker=FormatChecker(('email',)))

        errors = (error
                  for item in Path(folder).iterdir()
                  for error in _parse_errors(validator, item))
        try:
            print(next(errors), file=sys.stderr)
        except StopIteration:
            return 0
        else:
            for error in errors:
                print(error, file=sys.stderr)
            return 1

if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2:]))
