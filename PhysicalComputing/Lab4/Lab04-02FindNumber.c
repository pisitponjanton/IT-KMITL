#include <stdio.h>

int main()
{
    double a, b, c;
    scanf("%lf %lf %lf", &a, &b, &c);

    double min = a, max = a, sum;

    if (b < min) min = b;
    if (c < min) min = c;

    if (b > max) max = b;
    if (c > max) max = c;

    sum = a + b + c;

    printf("%.2lf", sum - (min + max));

    return 0;
}
