import sys
import lark
import argparse

grammar = """
?start: sheet

?sheet: rule*

rule: selector "{" block "}"

selector: NAME

block: declaration*

declaration: rule
           | NAME ":" NAME ";"

%import common.NUMBER
%import common.ESCAPED_STRING
%import common.CNAME -> NAME
%import common.WS_INLINE
%import common.WS
%import common.C_COMMENT
%import common.CPP_COMMENT

%ignore WS_INLINE
%ignore WS
"""

def main():
    cli_parser = argparse.ArgumentParser(prog='nss')
    cli_parser.add_argument('source', type=argparse.FileType('r'))
    cli_parser.add_argument('target', nargs='?',
                        type=argparse.FileType('w'), default=sys.stdout)
    args = cli_parser.parse_args()

    parser = lark.Lark(grammar, parser='lalr')
    tree = parser.parse(args.source.read())
    print(tree.pretty())

if __name__ == '__main__':
    main()
