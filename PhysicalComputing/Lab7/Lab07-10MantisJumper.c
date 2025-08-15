#include <stdio.h>

double ff(double x);

int main()
{
    int n;
    scanf("%d", &n);

    double sum = 1;
    for (int i = 1; i <= n / 2; i++)
    {
        double t = n - (i * 2);
        sum += ff(t + i) / (ff(t) * ff(i));
    }

    printf("method = %.0lf", sum);

    return 0;
}

double ff(double x)
{
    double sum = 1;
    for (int i = 1; i <= x; i++)
    {
        sum *= i;
    }
    return sum;
}