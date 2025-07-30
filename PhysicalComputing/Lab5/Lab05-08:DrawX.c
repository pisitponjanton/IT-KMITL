#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n / 2; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (j == i || j == n - i - 1)
            {
                printf("-");
            }
            else
            {
                printf("#");
            }
        }

        printf("\n");
    }

    for (int i = n / 2; i >= 0; i--)
    {
        for (int j = 0; j < n; j++)
        {
            if (j == i || j == n - i - 1)
            {
                printf("-");
            }
            else
            {
                printf("#");
            }
        }

        printf("\n");
    }
    return 0;
}