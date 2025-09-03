#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main()
{
    char *str = (char *)malloc(100 * sizeof(char));
    int lowercase = 0, uppercase = 0, digits = 0;

    scanf("%[^\n]", str);

    char *ptr = str;
    for (int i = 0; *(ptr + i) != '\0'; i++)
    {
        if (isdigit(*(ptr + i)))
            digits++;
        if (islower(*(ptr + i)))
            lowercase++;
        if (isupper(*(ptr + i)))
            uppercase++;
    }

    printf("Lowercase letters: %d\n", lowercase);
    printf("Uppercase letters: %d\n", uppercase);
    printf("Digits: %d", digits);

    free(str);
    return 0;
}