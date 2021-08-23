from utils import *

"""
Eval part of eval-apply mutually recursive structure. Eval takes lisp code
and converts it to our internal representation (a python list). It applies the
list using builtin functions written in apply.py, accessed using the symbol dict.
"""
def search(symbols, symbol):
    parent = symbols['$parent']
    assert type(symbol) != list, print(symbol)
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
    """
    Evaluate internal representation by returning numbers or applying procedures.
    Calls methods within apply by using the points to apply.py functions in the
    globals dict.
    """
    if (is_num(s)):
        return float(s)
    elif type(s) == str and search(symbols, s):
        return get(symbols, s)
    elif type(s) == list:
        name = s[0]
        if type(name) == list:
            name = evaluate(name, symbols)
        operands = s[1:]
        if search(symbols, name):
            func = get(symbols, name)
            symbols['$last'] = func(operands, symbols)
            return symbols['$last']
        else:
            raise NameError(f'name not found: {name}')
    return s
