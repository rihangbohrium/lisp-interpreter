"""
Read from interpreter and convert into internal representation.
For example: the string '(+ 2 2)' should be converted to
['+', 2.0, 2.0].
"""

whitespace = ['\n', '\t', ' ']

def read(prompt):
    prompt = len(prompt)*'.'
    s = ''
    sentinel = '' 
    first = True
    while True:
        line = input('' if first else prompt + ' ')
        s += line + '\n'
        for char in line:
            if char == ')':
                sentinel = sentinel[:-1] #error here means syntax issue
            elif char == '(':
                sentinel += ')'
        if sentinel == '':
            break
        if first:
            first = False
    return tokens(list(s))

def tokens(s):
    """
    Convert given list of chars into internal representation (python list).
    """
    assert type(s) == list

    parsed = []
    current = ''
    while len(s) > 0:
        char = s.pop(0)
        if (char == '(' or char == ')' or char in whitespace) and current != '':
            parsed.append(current)
            current = ''
        if char == '(':
            parsed.append(tokens(s))
        elif char == ')':
            return parsed
        elif char not in whitespace:
            current += char
    return parsed
        