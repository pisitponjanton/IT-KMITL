#include <stdio.h>

int main()
{
    char num[5];
    scanf("%s", num);
    printf("%-80.1s", num);
    printf("%-81.2s", num);
    printf("%-82.3s", num);
    printf("%-83.4s", num);
    printf("%-84.5s", num);
    return 0;
}