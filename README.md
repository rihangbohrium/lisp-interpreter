# lisp-interpreter
Object-less implementation of a lisp-language interpreter.
Uses the concept of the eval/apply mutual recursion structure, and Read-Eval-Print-Loop interpreter. Is based on 61A course project, but rewritten from scratch, again, using no objects or unique types other than lists and dicts.

![Eval and Apply recursion](https://evalapply.space/images/evalapply.jpeg)

# After cloning:
```
python main/interpreter.py
```
# Todo:
- custom error catching
- use define directly on a function, rather than requiring lambda
- add flag to read from file
