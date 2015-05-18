#include <stdio.h>
struct person
{
    int age;
};
char wat(void)
{
    struct person bob;
    bob.age = 19;
    return (char) bob.age;
}
int main(void)
{
    char huh = wat();
    putchar(huh);
}