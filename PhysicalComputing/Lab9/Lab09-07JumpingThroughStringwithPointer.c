#include <stdio.h>
#include <stdlib.h>

int main()
{
    int len, f;
    scanf("%d %d", &len, &f);
    char *str = (char *)malloc((len + 1) * sizeof(char));
    scanf(" %[^\n]", str);

    int i = 0;
    while (i <= len - 1 && *(str + i) != '\0')
    {
        printf("%c", *(str + i));
        i += f;
    }

    free(str);
    return 0;
}