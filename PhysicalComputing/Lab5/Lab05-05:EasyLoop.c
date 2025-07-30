#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);

    while (n != 0)
    {
        if (n > 0)
        {
            printf("%d ", n);
            n--;
        }
        else
        {
            printf("%d ", n);
            n++;
        }
    }
    printf("0");
}