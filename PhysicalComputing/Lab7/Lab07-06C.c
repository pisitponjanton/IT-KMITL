#include <stdio.h>
#include <math.h>

void printSqrt(double a, double b);

int main()
{
    double a, b;
    scanf("%lf %lf", &a, &b);
    printSqrt(a, b);
    return 0;
}

void printSqrt(double a, double b)
{
    double c = sqrt(a * a + b * b);
    printf("sqrt(%.0lf^2+%.0lf^2)=%.2lf", a, b, c);
}