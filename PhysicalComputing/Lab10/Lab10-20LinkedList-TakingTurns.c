#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    scanf("%d", &n);
    int *list = (int *)malloc(n * sizeof(int));
    int *pointer = list;

    for (int i = 0; i < n; i++)
    {
        scanf(" %d", &*(pointer + i));
    }

    int p = 0;
    int first = 0;
    int last = n - 1;

    for (int i = 0; i < n; i++)
    {
        if (p == 0 || p > 2)
        {
            printf("%d%s", *(pointer + (last--)), n - 1 == i ? "" : " -> ");
        }
        else
        {
            printf("%d%s", *(pointer + (first++)), n - 1 == i ? "" : " -> ");
        }
        p++;
        if (p == 5)
        {
            p = 1;
        }
    }

    free(list);
    return 0;
}