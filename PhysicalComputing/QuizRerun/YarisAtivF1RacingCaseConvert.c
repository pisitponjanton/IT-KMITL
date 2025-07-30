#include <stdio.h>

int main()
{
    char n;
    scanf("%c", &n);
    if (n >= 65 && n <= 90)
    {
        printf("%c", n + 32);
    }
    else if (n >= 97 && n <= 122)
    {
        printf("%c", n - 32);
    }
    else
    {
        printf("error");
    }

    return 0;
}