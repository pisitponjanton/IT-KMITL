#include <stdio.h>

int main()
{
    char g;
    scanf("%c", &g);
    switch (g)
    {
    case 'A':
    case 'a':
        printf("Genius");
        break;
    case 'B':
    case 'b':
        printf("Good");
        break;
    case 'C':
    case 'c':
        printf("Try Harder");
        break;
    case 'D':
    case 'd':
        printf("Very Bad");
        break;
    case 'F':
    case 'f':
        printf("Fail");
        break;
    default:
        printf("Invalid Input");
        break;
    }
    return 0;
}