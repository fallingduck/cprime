#include <stdio.h>
struct person
{
    int age;
};
char wat()
{
    struct person bob;
    bob.age = 19;
    return (char) bob.age;
}
int main()
{
    char huh = wat();
    putchar(huh);
}
