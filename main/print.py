from utils import is_num
import types

"""
Print portion of read-eval-print loop
"""
def print_repr(s):
    """
    Convert internal representation back to lisp code.
    """
    if s is None:
        return 'nil'
    if isinstance(s, bool):
        return '#t' if s else '#f'
    if is_num(s):
        return str(s)
    if isinstance(s, str):
        return s
    if isinstance(s, types.FunctionType):
        return f'(lambda ({print_repr(s(None, None, True))}))'
    r = ''
    for i in range(len(s)):
        expr = s[i]
        if type(expr) == list:
            r += f"({print_repr(expr)})"
        else:
            r += str(expr)
        if i < len(s)-1:
            r += ' '
    return r