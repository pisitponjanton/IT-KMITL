#include <stdio.h>

int main()
{
    int s, e, sum = 0;
    scanf("%d %d", &s, &e);
    printf("pass : ");
    for (int i = s; s < e ? i <= e : i >= e; s < e ? i++:i--)
    {
        if (i % 2 == 0)
        {
            printf("%d ", i);
            sum += i;
        }
    }
    printf("\n");
    printf("Sum : %d", sum);
    return 0;
}