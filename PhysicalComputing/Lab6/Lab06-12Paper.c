#include <stdio.h>

int main()
{
    char a1, a2;
    int x, y, sum = 1;
    scanf(" %c %d %c %d", &a1, &x, &a2, &y);

    for (int i = 1; i <= y - x; i++)
    {
        sum *= 2;
    }

    printf("%d", sum);
    return 0;
}