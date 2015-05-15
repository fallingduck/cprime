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

Support for single line code blocks: `if x: printf("Yes!")` or
`case 3: printf("Three")`

I think we might need a better way to split the code into logical "lines."
Consider the following example:

```
for (int i=0;
     i < 10;
     i++):
    printf("%d\n", i)
```

While the current system has support for escaped newlines (with a backslash),
those shouldn't be necessary for something like the above code.

Can this be distilled to one or two things to look for? Perhaps code surrounded
by parentheses and/or lines ending in `;`?
