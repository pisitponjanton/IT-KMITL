#include <stdio.h>

int main()
{
    float h, m;
    scanf(" %f", &h);
    scanf(" %f", &m);
    float hm = (h / 100) * (h / 100);
    printf("%f", m / hm);
    return 0;
}