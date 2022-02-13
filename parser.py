import lark
import argparse

grammar = """
start: sheet

sheet: rule*

rule: ""

%import common.NUMBER
%import common.ESCAPED_STRING
%import common.CNAME -> NAME
%import common.WS_INLINE
%import common.WS

%ignore WS_INLINE
%ignore WS
"""

def main():
    cli_parser = argparse.ArgumentParser(prog='nss')
    parser.add_argument('source', type=argparse.FileType('r'))
    parser.add_argument('target', nargs='?',
                        type=argparse.FileType('w'), default=sys.stdout)
    args = cli_parser.parse_args()

if __name__ == '__main__':
    main()
