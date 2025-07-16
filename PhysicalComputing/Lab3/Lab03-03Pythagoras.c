#include <stdio.h>
#include <math.h>

int main()
{
    double l, w;
    scanf(" %lf", &l);
    scanf(" %lf", &w);
    printf("%.2f", sqrt(l*l + w*w) );
    return 0;
}