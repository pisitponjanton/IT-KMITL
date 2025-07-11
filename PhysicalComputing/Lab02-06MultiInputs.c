#include <stdio.h>

int main()
{
    char str1[30], str2[30], str3[30], str4[30];

    scanf("%s", str1);
    scanf("%s", str2);
    scanf("%s", str3);
    scanf("%s", str4);

    printf("String 1: %.3s\n", str1);
    printf("String 2: %.4s\n", str2);
    printf("String 3: %.5s\n", str3);
    printf("String 4: %.6s\n", str4);

    return 0;
}
