#include <stdio.h>
#include <math.h>

double h(int deg, int u);

int main()
{
    int deg, u;
    scanf("%d %d", &deg, &u);
    printf("theta (degree) : %d\n", deg);
    printf("u (m/s) : %d\n", u);
    printf("h (m) : %.4f", h(deg, u));
    return 0;
}

double h(int deg, int u)
{
    return (pow(u, 2) * pow(sin((deg * M_PI) / 180.0), 2)) / (2 * 9.81);
}