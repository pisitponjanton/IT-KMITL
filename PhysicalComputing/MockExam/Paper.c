#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    int a, b;
    scanf("A%d", &a);
    scanf(" A%d", &b);
    printf("%.0f", pow(2, abs(a-b)));
    return 0;
}