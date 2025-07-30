#include <stdio.h>

int main()
{
    int age, day, price = 0;
    scanf("%d %d", &age, &day);

    if (day == 4)
    {
        price += 100;
    }
    else
    {
        if (day == 1 || day == 7)
        {
            price += 20;
        }
        if (age <= 12)
        {
            price += 120;
        }
        else if (age >= 13 && age <= 50)
        {
            price += 220;
        }
        else
        {
            price += 140;
        }
    }

    printf("Ticket price: %d Baht", price);
    return 0;
}