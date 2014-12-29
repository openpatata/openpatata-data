
"""Generate Markdown documentation for schemas. This script takes one
argument, which is the path to a schema.
"""

from collections import OrderedDict
import sys

import yaml


def _sort_dicts(val):
    """Recursively transform `dict`s into `OrderedDict`s and sort
    them alphabetically by their key.
    """
    if isinstance(val, dict):
        od = OrderedDict(sorted(val.items()))
        for k in od:
            od[k] = _sort_dicts(od[k])
        return od
    if isinstance(val, list):
        for i in range(len(val)):
            val[i] = _sort_dicts(val[i])
    return val


def _put_in_list(val):
    """Enclose non-lists within a list so that `str.join` won't split up
    strings.
    """
    if isinstance(val, list):
        # Make a copy of it 'cause we'll be modifying it in place.
        return list(val)
    else:
        return [val]


def _indent(count):
    """Markdown list item indentation. Expert stuff."""
    return '    '*count


def _fnp(format_string, tab, prefix='\n', *args, **kwargs):
    """Wrap `str.format` inside `print` for convenience. 'fnp' stands
    for 'format and print'.
    """
    print(('{prefix}{tab}{format_string}').format(
        prefix=prefix, tab=_indent(tab), format_string=format_string.format(
            *args, **kwargs)))


def main(schema):

    def _properties(schema, indent=0):
        """Print each property's name (key), accepted types (`type`)
        and values (`enum`), description (`description`) and whether
        it's required (`required`), and indent it appropriately.
        Examples:

        * [required] **`pages`** (string|number)

            The page or pages this passage is found on.

        * **`type`** (string|null)

            The type of publication.

            One of:

            * 'magazine'
            * 'journal'
            * 'newspaper'
        """
        # If schema is of type `array`, look for the properties inside
        # `items`.
        if 'array' in schema['type']:
            properties = schema['items']
            # `items` may be a list, which defines a different schema
            # for each item, in the order that they appear (see
            # http://spacetelescope.github.io/understanding-json-schema/reference/array.html#tuple-validation).
            if isinstance(properties, list):
                for item in properties:
                    # Each schema is an item inside a numbered list.
                    _fnp('1. ', indent)
                    _properties(item, indent+1)
            # Otherwise, ut should be a dictionary, like any other
            # schema.
            else:
                _properties(properties, indent)

        properties = schema.get('properties')
        if properties:
            for k, v in properties.items():
                # Join types with a vertical bar and place the type of
                # items of regular arrays inside square brackets,
                # e.g. `array [object]|null`
                type_ = _put_in_list(v['type'])
                try:
                    array = type_.index('array')
                except ValueError:
                    pass
                else:
                    items = v['items']
                    if isinstance(items, dict) and 'type' in items:
                        type_[array] = 'array [{sub_type}]'.format(
                            sub_type='|'.join(_put_in_list(items['type'])))
                type_ = '|'.join(type_)

                _fnp(
                    '* {is_req}**`{k}`** (`{type_}`)', indent,
                    is_req=('[required] ' if k in schema.get(
                        'required', []) else ''), k=k, type_=type_)

                description = v.get('description', '').strip()
                if description:
                    _fnp(
                        '{description}', indent+1,
                        description=description)

                enum = v.get('enum')
                if enum:
                    _fnp('One of:\n', indent+1)
                    [_fnp(
                        '* {item}', indent+1, '',
                        item=i) for i in enum]

                _properties(v, indent+1)
        else:
            # Complex definitions
            for item in ('allOf', 'anyOf', 'oneOf'):
                try:
                    special = schema[item]
                except KeyError:
                    pass
                else:
                    _fnp(
                        'Each item must be compliant with {item}:',
                        indent, item={
                            'allOf': 'all of',
                            'anyOf': 'any of',
                            'oneOf': 'exactly one of'}[item])
                    for special in special:
                        _fnp('* ', indent)
                        _properties(special, indent+1)

    with open(schema) as f:
        schema = _sort_dicts(yaml.load(f.read()))
        _properties(schema)


if __name__ == '__main__':
    main(sys.argv[1])
