
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
        # Make a copy of it 'cause we might be modifying it in place.
        return list(val)
    else:
        return [val]


def _fnp(format_string, *args, **kwargs):
    """Wrap `str.format` inside `print` for convenience. 'fnp' stands
    for 'format and print'.
    """
    print(format_string.format(*args, **kwargs))


def _indent(count):
    """Markdown list item indentation. Expert stuff."""
    return '    '*count


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
        if 'array' in schema['type']:
            properties = schema['items']
            if isinstance(properties, list):
                for item in properties:
                    _fnp('\n{tab}1. ', tab=_indent(indent))
                    _properties(item, indent+1)
            else:
                _properties(properties, indent)

        properties = schema.get('properties')
        if properties:
            for k, v in properties.items():
                # Join types with a vertical bar and place the type of
                # array items of regular arrays inside square brackets,
                # e.g. `array [object]|null`.
                type_ = _put_in_list(v['type'])
                if 'array' in type_:
                    if isinstance(v['items'], dict) and 'type' in v['items']:
                        type_[type_.index('array')] = \
                            'array [{sub_type}]'.format(
                                sub_type='|'.join(_put_in_list(
                                    v['items']['type'])))
                type_ = '|'.join(type_)

                # Headline on a new paragraph.
                _fnp(
                    '\n{tab}* {is_req}**`{k}`** (`{type_}`)',
                    tab=_indent(indent),
                    is_req=('[required] ' if k in schema.get(
                        'required', []) else ''), k=k, type_=type_)

                # Description on a new paragraph.
                description = v.get('description', '').strip()
                if description:
                    _fnp(
                        '\n{tab}{description}',
                        tab=_indent(indent+1), description=description)

                # Accepted values on a new paragraph.
                enum = v.get('enum')
                if enum:
                    _fnp(
                        '\n{tab}One of:\n{enum}',
                        tab=_indent(indent+1),
                        enum=''.join('\n{tab}* {i}'.format(
                            tab=_indent(indent+1), i=i) for i in enum))

                _properties(v, indent+1)
        else:
            # Complex definitions.
            for item in ('allOf', 'anyOf', 'oneOf'):
                try:
                    special = schema[item]
                except KeyError:
                    pass
                else:
                    _fnp(
                        '\n{tab}Each item must be compliant with {item}:\n',
                        tab=_indent(indent), item={
                            'allOf': 'all of',
                            'anyOf': 'any of',
                            'oneOf': 'exactly one of'}[item])
                    for special in special:
                        _fnp('{tab}* ', tab=_indent(indent))
                        _properties(special, indent+1)

    with open(schema) as f:
        items = _sort_dicts(yaml.load(f.read()))
        _properties(items)


if __name__ == '__main__':
    main(sys.argv[1])
