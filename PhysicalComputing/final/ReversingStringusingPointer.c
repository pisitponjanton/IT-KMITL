#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *str, text;
    int size = 0, cap = 100;

    str = (char *)malloc(cap * sizeof(char));

    scanf("%[^\n]", str);

    while (*(str + size) != '\0')
    {
        size++;
    }

    for (int i = size - 1; i >= 0; i--)
    {
        printf("%c", *(str + i));
    }

    return 0;
}