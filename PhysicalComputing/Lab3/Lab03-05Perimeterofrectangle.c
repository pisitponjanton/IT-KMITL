#include <stdio.h>

int main()
{
    double x, y;
    scanf("%lf", &x);
    scanf("%lf", &y);
    printf("Perimeter of rectangle = %.4lf units",x*2 + y*2);
    return 0;
}