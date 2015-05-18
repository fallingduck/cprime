#include <stdio.h>
void loop1(void)
{
    for (int x = 0; x < 10; x++)
    {
        printf("%d\n", x);
    }
}
void loop2(void)
{
    int x = 0;
    while (x < 10)
    {
        printf("%d\n", x);
        x++;
    }
}
void loop3(void)
{
    int x;
    x = 0;
    do
    {
        printf("Hello, World!\n");
    }
    while (x != 0);
}
int main(void)
{
    loop1();
    loop2();
    loop3();
}