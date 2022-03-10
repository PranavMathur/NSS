import sys
import lark
import argparse

grammar = """
?start: sheet

?sheet: rule*

rule: selector "{" block "}"

selector: /[a-z]+/i

block: declaration*

declaration: rule
           | property ":" value ";"

property: /[a-z-]+/i

value: NAME
     | /#[a-f0-9]+/i -> rgb

%import common.NUMBER
%import common.ESCAPED_STRING
%import common.CNAME -> NAME
%import common.WS_INLINE
%import common.WS
%import common.C_COMMENT
%import common.CPP_COMMENT

%ignore WS_INLINE
%ignore WS
%ignore C_COMMENT
%ignore CPP_COMMENT
"""

def main():
    cli_parser = argparse.ArgumentParser(prog='nss')
    cli_parser.add_argument('source', type=argparse.FileType('r'))
    cli_parser.add_argument('target', nargs='?',
                        type=argparse.FileType('w'), default=sys.stdout)
    args = cli_parser.parse_args()

    parser = lark.Lark(grammar, parser='lalr')
    try:
        tree = parser.parse(args.source.read())
    except lark.exceptions.LarkError as e:
        print(e)
        exit(1)
    print(tree.pretty())

if __name__ == '__main__':
    main()
