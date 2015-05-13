### First Pass
1. (DONE) Strip comments
2. (DONE) CPP commands carry through
3. (DONE) `include` keywords get changed to `#include`
4. (DONE) Handle colon plus indentation -> brackets, except with `case`
5. (DONE) Handle `default` keyword
6. `continue` statement in `case` blocks to provide a "fall-through"
7. Single line blocks

### Comments

Move individual tests out of `primec.py`!

Passing `void` to a function is ugly and pretty much unnecessary, because
variable argument functions are generally not good ideas anyway. I'm going the
C++ route here, I think, so `void f()` should become `void f(void)` in the
compiled code.

Preprocessor commands for C-Prime? Mainly thinking about an `include` command
which tags header files to be transpiled.
