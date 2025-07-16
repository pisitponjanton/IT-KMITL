#include <stdio.h>

int main()
{
    char num[5];
    scanf("%s", num);
    printf("%-81.1s", num);
    printf("%-81.2s", num);
    printf("%-81.3s", num);
    printf("%-81.4s", num);
    printf("%.5s", num);
    return 0;
}