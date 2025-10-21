#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *str;
    int size = 0, capacity = 10;

    str = (char *)malloc(capacity * sizeof(char));

    char text;
    while (1)
    {
        scanf(" %c", &text);
        if (text == '-')
        {
            break;
        }

        if (size >= capacity)
        {
            capacity *= 2;
            str = (char *)realloc(str, capacity * sizeof(char));
        }

        *(str + size) = text;
        size++;
    }

    for (int i = 0; i < size; i++)
    {
        printf("%c", *(str + i));
    }
    printf("\n");

    for (int i = size-1; i >= 0; i--)
    {
        printf("%c", *(str + i));
    }
    printf("\n");

    free(str);

    return 0;
}