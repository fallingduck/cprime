### First Pass
1. Strip comments
2. CPP commands carry through
3. `include` keywords get changed to `#include`
4. Handle colon plus indentation -> brackets, except with `case`
5. Handle `default` keyword
8. C-Prime preprocessor commands

### Second Pass
1. Add parentheses where required
2. Add semicolons where required
3. Replace `and` and `or` keywords with binary operators
4. Single line block parsing
5. Automatically pass `void` to no-argument function definitions

### Post-Processing
1. Handle transpiling includes
