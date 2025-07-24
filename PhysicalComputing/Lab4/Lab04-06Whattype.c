#include <stdio.h>

int main()
{
    char input;
    scanf("%c", &input);

    if (input >= 48 && input <= 57)
    {
        printf("number");
    }
    else if (input >= 97 && input <= 122)
    {
        printf("lowercase");
    }
    else if (input >= 65 && input <= 90)
    {
        printf("uppercase");
    }
    else
    {
        printf("error");
    }
    return 0;
}