#include <stdio.h>

int main()
{
    int a20 = 0, a_20 = 0, a30 = 0, a40 = 0;
    int all_age = 0, all_height = 0, all_weight = 0;

    for (int i = 0; i < 50; i++)
    {
        int age = 0, height = 0, weight = 0;
        scanf("%d %d %d", &age, &height, &weight);

        all_age += age;
        all_height += height;
        all_weight += weight;

        if (age >= 20 && height >= 160)
        {
            ++a20;
        }
        if (age < 20 && (height <= 180 || weight >= 60))
        {
            ++a_20;
        }
        if (age >= 30 && weight >= 40 && weight <= 80)
        {
            ++a30;
        }
        if (age < 40 &&( weight < 85 || height <= 200))
        {
            ++a40;
        }
    }

    printf("Age >= 20 and Height >= 160: %d\n", a20);
    printf("Age < 20 and Height <= 180 or Weight >= 60: %d\n", a_20);
    printf("Age >= 30 and Weight >= 40 and Weight <= 80: %d\n", a30);
    printf("Age < 40 and Weight < 85 or Height <= 200: %d\n", a40);
    printf("Average Age: %d\n", all_age / 50);
    printf("Average Height: %.2f\n", all_height / 50.0);
    printf("Average Weight: %.2f\n", all_weight / 50.0);
    return 0;
}