from sys import exit

from read import *
from eval import *
from print import *
import apply

def repl(prompt='lisp>'):
    print("""rb-lisp, a lisp language interpreter.\nGitHub: https://github.com/rihangbohrium/lisp-interpreter""")


    symbols = apply.get_globals()
    while True:
        print(prompt, end=' ')
        to_eval = read(prompt)
        for expr in to_eval:
            print(print_repr(evaluate(expr, symbols)))

if __name__ == '__main__':
    repl()