#include <stdio.h>

int main()
{
    double num;
    scanf("%lf", &num);
    if (num >= 0 && num < 48.697)
    {
        printf("Ayutthaya");
    }
    else if (num >= 48.697 && num < 66.456)
    {
        printf("Ang Thong");
    }
    else if (num >= 66.456 && num < 84.918)
    {
        printf("Sing Buri");
    }
    else if (num >= 84.918 && num < 85.900)
    {
        printf("Lop Buri");
    }
    else if (num >= 85.900 && num < 111.936)
    {
        printf("Sing Buri");
    }
    else if (num >= 111.936 && num < 150.019)
    {
        printf("Chai Nat");
    }
    else if (num >= 150.019 && num < 150.545)
    {
        printf("Nakhon Sawan");
    }
    else
    {
        printf("InValid");
    }
    return 0;
}