#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *str;

    str = (char *)malloc(100 * sizeof(char));

    scanf("%[^\n]", str);

    char *ptr = str;
    int size = 0;
    for (int i = 0; *ptr++ != '\0'; i++)
    {
        size++;
    }

    ptr = str;
    for (int i = size - 1; i >= 0; i--)
    {
        printf("%c", *(ptr + i));
    }

    free(str);

    return 0;
}