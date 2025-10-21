#include <stdio.h>
#include <stdlib.h>

int main()
{
    long n, a, b, c, d, e, f, g;
    scanf("%ld %ld %ld %ld %ld %ld %ld %ld", &n, &a, &b, &c, &d, &e, &f, &g);

    long gap = labs(f - g);
    long price;

    if (f > n || g > n || f < 0 || g < 0)
    {
        printf("Error");
        return 0;
    }

    if (gap <= a)
    {
        price = b;
    }
    else if (gap <= a + c)
    {
        price = b + (gap - a) * d;
    }
    else
    {
        price = b + c * d + (gap - a - c) * e;
    }

    printf("%ld", price);
    return 0;
}
