from utils import *

"""
Evaluate and apply internal representation.
"""
def search(symbols, symbol):
    parent = symbols['$parent']
    if symbol in symbols.keys():
        return True 
    elif parent is not None:
        return search(parent, symbol)
    raise LookupError(f"symbol not found: {symbol}")

def get(symbols, symbol):
    parent = symbols['$parent']
    if symbol in symbols.keys():
        return symbols[symbol] 
    elif parent is not None:
        return get(parent, symbol)
    else:
        assert False, "symbol not found"

def evaluate(s, symbols):
    if (is_num(s)):
        return float(s)
    elif type(s) == str and search(symbols, s):
        return get(symbols, s)
    elif type(s) == list:
        name = s[0]
        operands = s[1:]
        if search(symbols, name):
            func = get(symbols, name)
            return func(operands, symbols)
        else:
            raise NameError(f'name not found: {name}')
    return s
