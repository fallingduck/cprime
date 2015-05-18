### First Pass
1. (DONE) Strip comments
2. (DONE) CPP commands carry through
3. (DONE) `include` keywords get changed to `#include`
4. (DONE) Handle colon plus indentation -> brackets, except with `case`
5. (DONE) Handle `default` keyword
8. (DONE) C-Prime preprocessor commands

### Second Pass
1. (DONE) Add parentheses where required
2. (DONE) Add semicolons where required
3. (DONE) Replace `and` and `or` keywords with binary operators
4. (DONE) Single line block parsing
5. (DONE) Automatically pass `void` to no-argument function definitions

### Post-Processing
1. Handle transpiling includes

### Comments

Eventually it would be great if `primec` could produce C code with comments that
carry over from the C-Prime code.

Move individual searches out of `primec.py`! -- Probably not going to happen,
because `primec.py` is only a temporary script. The final product written in
C-Prime will be neater, to be sure.
