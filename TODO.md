### First Pass
1. (DONE) Strip comments
2. (DONE) CPP commands carry through
3. (DONE) `include` keywords get changed to `#include`
4. (DONE) Handle colon plus indentation -> brackets, except with `case`
5. (DONE) Handle `default` keyword
8. (DONE) C-Prime preprocessor commands

### Second Pass
(DONE) This mostly focusses on adding in parentheses where required, adding
semicolons where required, and converting keywords like `and`, `or`, and `not`
to their respective C operators.

(DONE) List of keywords that need to be parsed/parentheses need to be added to:
```
if
switch
case
while
```

### Post-Processing
1. Handle transpiling includes

### Comments

Make `linesanstrings` work...

Support for single line code blocks: `if x: printf("Yes!")` or
`case 3: printf("Three")`

Passing `void` to a function is ugly and pretty much unnecessary, because
non-specified argument functions are generally not good ideas anyway. I'm going
the C++ route here, I think, so `void f()` should become `void f(void)` in the
compiled code.

Eventually it would be great if `primec` could produce C code with comments that
carry over from the C-Prime code.

Move individual searches out of `primec.py`! -- Probably not going to happen,
because `primec.py` is only a temporary script. The final product written in
C-Prime will be neater, to be sure.
