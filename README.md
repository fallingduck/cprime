# C-Prime

**MILESTONE 5/16/2015: All basic test programs (`examples/`) compile**

C-Prime is C without all the clutter. Inspired in part by CoffeeScript's
makeover of JavaScript, C-Prime believes that C can become more beautiful,
more readable, and easier to write. C-Prime is not a new language, however. It
is simply a more beautiful way of writing C code. C-Prime code then gets
directly transpiled to C code, to be compiled by your system's C compiler.

Basically, C-Prime doesn't get in the way of C grammar, but provides a less
cluttered (and in some cases less error-prone) way of writing it.

### 1.0????

Haha, good one m8. Right now, C-Prime is in a "pre-release" state. This means
that it should *not* be used to write programs, although you can still play
around with the compiler a bit.

Right now, the compiler is (ironically?) being written in Python, because
Python made it easier to just get off the ground with the project. You know
what would be cool though? A C-Prime compiler *written in C-Prime*!!1!1

Once `primec` has been rewritten in C-Prime and successfully compiled with
`primec.py`, then the language will be ready for the "stable beta" 0.1 release.

1.0 is but a distant dream at this point.

### Example programs:

```
include <stdio.h>

struct person:
    char[20] name
    int age

void wat():
    struct person bob
    bob.name = "Bob"
    bob.age = 19
```

```
include <stdio.h>

int main():
    printf("Shall we play a game?\n")
    printf("1. Hearts\n")
    printf("2. Chess\n")
    printf("3. Theaterwide Biotoxic And Chemical Warfare\n\n")
    printf("4. Global Thermonuclear War\n\n")

    int input
    scanf("%d", &input)
    switch input:
        case 1:
            printf("You chose: Hearts\n")
        case 2:
            printf("You chose: Chess\n")
        case 3:
            printf("You chose: Theaterwide Biotoxic and Chemical Warfare\n")
        case 4:
            printf("How about a nice game of chess?\n")
        default:
            printf("Bye!")
    return 0
```

```
include <stdio.h>

void loop1():
    for (int x = 0; x < 10; x++):
        printf("%d\n", x)

void loop2():
    int x = 0
    while x < 10:
        printf("%d\n", x)
        x++

void loop3():
    int x
    x = 0
    do:
        // "Hello, World!" is printed one time
        printf("Hello, World!\n")
    while x != 0
```
