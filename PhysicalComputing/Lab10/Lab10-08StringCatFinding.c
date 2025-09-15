#include <stdio.h>
#include <ctype.h>

int main()
{
    char str[2000];
    scanf("%[^\n]", str);

    int first = 1;

    for (int i = 0; str[i] != '\0'; i++)
    {
        if (tolower(str[i]) == 'c' && 
            tolower(str[i + 1]) == 'a' && 
            tolower(str[i + 2]) == 't')
        {
            if (!first) {
                printf(", ");
            }
            printf("%d", i);
            first = 0;
        }
    }

    printf("\n");
    return 0;
}
