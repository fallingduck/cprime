#include <stdio.h>
int main(void)
{
    printf("Shall we play a game?\n");
    printf("1. Hearts\n");
    printf("2. Chess\n");
    printf("3. Theaterwide Biotoxic And Chemical Warfare\n\n");
    printf("4. Global Thermonuclear War\n\n");
    int input;
    scanf("%d", &input);
    switch (input)
    {
        case 1:
            printf("OK\n");
            break;
        case 2:
            printf("OK\n");
            break;
        case 3:
            printf("OK\n");
            break;
        case 4: printf("How about a nice game of chess?\n"); break;
        default:
            printf("Bye!");
            break;
    }
    return 0;
}