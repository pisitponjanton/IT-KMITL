#include <stdio.h>
#include <math.h>

void perimeter(double x, double y);
void area(double x, double y);
int main()
{
    double a, b;
    scanf("%lf %lf", &a, &b);
    perimeter(a, b);
    area(a, b);
    return 0;
}

void perimeter(double x, double y)
{
    double c = sqrt(x * x + y * y);
    printf("Perimeter: %.2lf\n", c+y+x);
}

void area(double x, double y)
{
    double c = (x*y)/2;
    printf("Area: %.2lf\n", c);
}