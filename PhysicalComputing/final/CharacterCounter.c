#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main()
{
    char *str;
    int size = 0, low = 0, up = 0, dig = 0;

    str = (char *)malloc(101 * sizeof(char));
    scanf("%[^\n]", str);

    while (*(str + size) != '\0')
    {
        char s = *(str + size);
        if (islower(s))
            low++;
        else if (isupper(s))
            up++;
        else if (isdigit(s))
            dig++;
        size++;
    }

    printf("Lowercase letters: %d\n", low);
    printf("Uppercase letters: %d\n", up);
    printf("Digits: %d\n", dig);

    return 0;
}