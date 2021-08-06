from eval import evaluate

def get_globals():
    return global_symbols

def eval_all(ops, symbols):
    for i in range(len(ops)):
        ops[i] = evaluate(ops[i], symbols)

def add(ops, symbols=None):
    eval_all(ops, symbols)
    return sum(ops)

def subtract(ops, symbols=None):
    eval_all(ops, symbols)
    return ops[0] - sum(ops[1:])

def multiply(ops, symbols=None):
    eval_all(ops, symbols)
    r = 1
    for i in ops:
        r *= i
    return r

def divide(ops, symbols=None):
    eval_all(ops, symbols)
    r = ops[0]
    for i in ops[1:]:
        r /= i
    return r

def define(ops, symbols):
    assert type(ops[0]) == str
    symbols[ops[0]] = evaluate(ops[1], symbols)
    return ops[0]

global_symbols = {'$parent' : None, 
                '$': lambda x : 5,
                '+': add,
                '-': subtract,
                '*': multiply,
                '/': divide,
                'define': define
                }