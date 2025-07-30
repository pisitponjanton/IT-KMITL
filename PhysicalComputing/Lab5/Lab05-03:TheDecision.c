#include <stdio.h>

int main()
{
    int m, n;
    scanf("%d %d", &m, &n);

    if (m > n)
    {
        for (int i = m; i >= n; i--)
        {
            printf("%d ", i);
        }
    }
    else
    {
        for (int i = m; i <= n; i++)
        {
            printf("%d ", i);
        }
    }
    return 0;
}