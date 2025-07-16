#include <stdio.h>

int main()
{
    double raka, d, h;
    scanf(" %lf", &raka);
    scanf(" %lf", &d);
    scanf(" %lf", &h);
    double v = 3.14159265359 * (d/2)*(d/2) *h;
    printf("Volume : %.2lfml\n",v);
    printf("Baht/ml : %.4lf", raka/v);
    return 0;
}