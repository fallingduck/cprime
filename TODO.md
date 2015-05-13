### First Pass
1. (DONE) Strip comments
2. (DONE) Preprocessor commands carry through
3. (DONE) `include` keywords get changed to `#include`
4. (DONE) Handle colon plus indentation -> brackets, except with `case`
5. (DONE) Handle `default` keyword
6. Single line blocks

### Comments

Passing `void` to a function is ugly and pretty much unnecessary, because
variable argument functions are generally not good ideas anyway. I'm going the
C++ route here, I think, so `void f()` should become `void f(void)` in the
compiled code.
