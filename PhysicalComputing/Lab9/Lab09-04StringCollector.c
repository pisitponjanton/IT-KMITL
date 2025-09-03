#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *str, s;
    int size = 0, capacity = 10;
    str = (char *)malloc(capacity * sizeof(char));

    while (1)
    {
        scanf(" %c", &s);
        if (s == '-')
        {
            *(str + size) = '\0';
            break;
        }

        if (size >= capacity)
        {
            capacity *= 2;
            str = (char *)realloc(str, capacity * sizeof(char));
        }

        *(str + size) = s;
        size++;
    }

    char *ptr = str;
    while (*ptr != '\0')
    {
        printf("%c", *ptr++);
    }
    printf("\n");
    ptr = str;
    for (int i = size-1; i >= 0; i--)
    {
        printf("%c", *(ptr + i));
    }

    free(str);
    return 0;
}