from eval import evaluate
import utils

"""
The apply part of eval-apply recursion construct. Contains python implementation for the
Lisp builtin procedures. Because python does not allow circular imports, this file 
imports eval.py, but eval.py does not import this, instead accessing these functions
from global_symbols dict. 
"""

def get_globals():
    return global_symbols

def eval_all(ops, symbols):
    for i in range(len(ops)):
        ops[i] = evaluate(ops[i], symbols)

# Built-in Functions

def equals(ops, symbols):
    eval_all(ops, symbols)
    return ops[0] == ops[1]

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
    assert type(ops[0]) == str, print(ops)
    assert utils.valid_name(ops[0]), f'Name not valid: {ops[0]}'
    symbols[ops[0]] = evaluate(ops[1], symbols)
    return str(ops[0])

def lisp_lambda(ops, symbols):
    """
    We do be dynamic scoping xDDDDDD
    """
    declared_scope = {'$parent':symbols}
    vars = ops[0]
    def when_called(args, sym=None, get_args=False):
        if get_args:
            return ops[0]
        assert len(ops[0]) == len(args)
        for i in range(len(args)):
            # evaluate arguments in scope where function is called
            # define scope where function was defined (ie new_scope)
            if not utils.is_num(vars[i]):
                define([vars[i], args[i]], sym)
        for expr in ops[1:]:
            evaluate(expr, sym)
        return evaluate(ops[-1], sym)
    return when_called

def lisp_if(ops, symbols):
    if evaluate(ops[0], symbols):
        return evaluate(ops[1], symbols)
    return evaluate(ops[2], symbols)

def lisp_cond(ops, symbols):
    for expr in ops:
        if evaluate(expr[0], symbols):
            return evaluate(expr[1], symbols)
        

global_symbols = {'$parent' : None, 
                '#t': True,
                '#f': False,
                'nil': None,
                'else': True,
                '=': equals,
                '+': add,
                '-': subtract,
                '*': multiply,
                '/': divide,
                'define': define,
                'lambda':lisp_lambda,
                'if': lisp_if,
                'cond': lisp_cond
                }
