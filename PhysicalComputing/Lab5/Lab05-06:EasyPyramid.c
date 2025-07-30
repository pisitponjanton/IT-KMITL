#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);

    int n_1 = n;
    for (int i = 1; i <= n; i++)
    {
        for (int j = n_1 - 1; j > 0; j--)
        {
            printf(" ");
        }

        for (int j = i; j <= i*3 - 2; j++)
        {
            printf("*");
        }
        printf("\n");
        n_1--;
    }
    return 0;
}