### First Pass
1. (DONE) Strip comments
2. (DONE) CPP commands carry through
3. (DONE) `include` keywords get changed to `#include`
4. (DONE) Handle colon plus indentation -> brackets, except with `case`
5. (DONE) Handle `default` keyword
8. (DONE) C-Prime preprocessor commands

### Post-Processing
1. Handle transpiling includes

### Comments

Move individual searches out of `primec.py`!

Passing `void` to a function is ugly and pretty much unnecessary, because
non-specified argument functions are generally not good ideas anyway. I'm going
the C++ route here, I think, so `void f()` should become `void f(void)` in the
compiled code.

How to handle unnamed structures? Example:
`struct {int employee_id; float salary;} bob`

Support for single line code blocks: `if x: printf("Yes!")`
