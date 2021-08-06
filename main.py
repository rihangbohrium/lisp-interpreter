from sys import exit

from read import *
from eval import *
from print import *
import apply

def repl(prompt='scm>'):
    """
    Base logic of interpreter, using Read-Eval-Print-Loop structure
    """
    symbols = apply.get_globals()
    prompt += ' '
    while True:
        print(prompt, end='')
        to_eval = read()
        for expr in to_eval:
            print(print_repr(evaluate(expr, symbols)))

if __name__ == '__main__':
    repl()