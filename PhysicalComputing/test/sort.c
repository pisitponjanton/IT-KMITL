#include <stdio.h>

void swap(int *p, int *q);
void bubble(int a[], int n);

int main()
{
    int n;
    scanf(" %d", &n);
    int NUM[n];

    for (int i = 0; i < n; i++)
    {
        scanf(" %d", &NUM[i]);
    }

    bubble(NUM, n);

    for (int i = 0; i < n; i++)
    {
        printf("%d ", NUM[i]);
    }

    return 0;
}

void swap(int *p, int *q)
{
    int tmp;
    tmp = *p;
    *p = *q;
    *q = tmp;
}

void bubble(int a[], int n)
{
    for (int i = 0; i < n - 1; ++i)
    {
        for (int j = n - 1; j > i; --j)
        {
            if (a[j - 1] > a[j])
            {
                swap(&a[j - 1], &a[j]);
            }
        }
    }
}