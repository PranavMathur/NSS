import lark

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
