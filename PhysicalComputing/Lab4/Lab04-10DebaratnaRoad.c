#include <stdio.h>

int main()
{
    double kg;
    scanf("%lf", &kg);

    if (kg >= 0 && kg <= 5.032)
    {
        printf("Bangkok");
    }
    else if (kg > 5.032 && kg <=  35.477)
    {
        printf("Samut Prakarn");
    }
    else if (kg > 35.477 && kg <= 52.9)
    {
        printf("Chachoengsao");
    }
    else if (kg > 52.9 && kg <= 58.855)
    {
        printf("Chon Buri");
    }
    else
    {
        printf("InValid");
    }
    return 0;
}