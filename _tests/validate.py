
import os
import sys

import jsonschema
import yaml


def validate(folder):
    """checks our data for syntax errors and compliance with the schema"""
    with open(os.path.join('_tests', 'schemas',
                           '{}.yaml'.format(folder.rstrip('s/')))) as schema:
        validator = jsonschema.Draft4Validator(
            yaml.load(schema),
            format_checker=jsonschema.FormatChecker(['date']))

    for item in os.listdir(folder):
        with open(os.path.join(folder, item)) as item_:
            errors = list(validator.iter_errors(yaml.load(item_)))
            if errors:
                print(os.path.join(folder, item))
                for error in errors:
                    print('- [{}] {}'.format('/'.join(map(str, error.path)),
                                             error.message))

if __name__ == '__main__':
    validate(sys.argv[1])
