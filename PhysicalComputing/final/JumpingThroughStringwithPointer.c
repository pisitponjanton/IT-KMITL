#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, m, size = 0;
    char *str;
    scanf(" %d", &n);
    scanf(" %d", &m);
    str = (char *)malloc(n * sizeof(char));
    scanf(" %[^\n]", str);
    while (*(str + size) != '\0')
    {
        printf("%c", *(str + (size)));
        size += m;
    }

    return 0;
}