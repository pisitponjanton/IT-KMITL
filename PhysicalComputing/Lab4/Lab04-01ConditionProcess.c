#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    if (a == b)
    {
        printf("%d + %d = %d", a, b, a + b);
    }
    else
    {
        printf("%d - %d = %d", a, b, a - b);
    }
    return 0;
}