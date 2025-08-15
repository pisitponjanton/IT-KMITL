#include <stdio.h>

int main()
{
    double fuel_price;
    int is_exprees[4];
    double ps[4];

    scanf(" %lf", &fuel_price);
    for (int i = 0; i < 4; i++)
    {
        scanf(" %d", &is_exprees[i]);
    }

    for (int i = 0; i < 4; i++)
    {
        scanf(" %lf", &ps[i]);
    }

    double avg1 = 0, avg2 = 0;
    int c1 = 0, c2 = 0;
    for (int i = 0; i < 4; i++)
    {
        double lit, cost;

        if (is_exprees[i])
        {
            lit = 29.0 / ps[i];
            cost = (lit * fuel_price) + 60.0;
            avg1 += cost;
            c1++;
        }
        else
        {
            lit = 25.0 / ps[i];
            cost = lit * fuel_price;
            avg2 += cost;
            c2++;
        }

        printf("Day %d: fuel %.2f L, cost %.2f Baht\n", i + 1, lit, cost);
    }
    printf("Expressway: %.2f Baht\n", c1 ? avg1 / c1 : 0);
    printf("Romklao: %.2f Baht",c2 ? avg2 / c2: 0);

    return 0;
}