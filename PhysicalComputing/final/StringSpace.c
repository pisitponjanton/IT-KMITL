#include <stdio.h>
#include <string.h>

int main()
{
    char str[150];
    scanf("%[^\n]", str);

    for (int i = 0; str[i] != '\0'; i++)
    {
        if (str[i] != ' ')
        {
            printf("%c", str[i]);
        }
    }

    return 0;
}