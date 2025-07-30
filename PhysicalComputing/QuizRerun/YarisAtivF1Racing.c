#include <stdio.h>

int main()
{
    int save, n, n_save, count = 0;
    float d;
    scanf("%d %f %d %d", &save, &d, &n, &n_save);

    if (save == 0)
    {
        count++;
    }
    if (n <= 2)
    {
        count++;
    }
    if (d >= 1)
    {
        count++;
    }
    if (n - n_save <= 1)
    {
        count++;
    }
    if (count == 0)
    {
        printf("DRS allowed");
    }
    else
    {
        printf("DRS not allowed %d", count);
    }
    return 0;
}