#include <stdio.h>

int main()
{
    int M[] = {2, 20, 8, 10, 4, 6, 16, 18};
    int N[] = {1, 3, 9, 7, 11, 15, 19};

    int n;
    while (1)
    {
        scanf("%d", &n);
        if (n >= 1 && n <= 20)
        {
            break;
        }
    }

    for (int i = 0; i < 8; i++)
    {
        if (M[i] == n)
        {
            printf("%d is in M at index [%d]", n, i);
            return 0;
        }
    }

    for (int i = 0; i < 7; i++)
    {
        if (N[i] == n)
        {
            printf("%d is in N at index [%d]", n, i);
            return 0;
        }
    }

    printf("%d is not in neither M nor N",n);

    return 0;
}