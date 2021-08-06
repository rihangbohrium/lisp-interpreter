from utils import is_num

"""
Print portion of read-eval-print loop
"""
def print_repr(s):
    """
    get python list representation, return as string
    """
    if is_num(s):
        return str(s)
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