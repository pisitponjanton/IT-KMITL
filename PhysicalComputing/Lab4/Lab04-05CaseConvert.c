#include <stdio.h>

int main()
{
    char input;
    scanf("%c", &input);
    if (input >= 65 && input <= 90)
    {
        printf("%c", input + 32);
    }
    else if (input >= 97 && input <= 122)
    {
        printf("%c", input - 32);
    }
    else{
        printf("error");
    }

    return 0;
}