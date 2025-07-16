#include <stdio.h>

int main()
{
    float n1, n2, n3, n4;
    scanf(" %f", &n1);
    scanf(" %f", &n2);
    scanf(" %f", &n3);
    scanf(" %f", &n4);
    printf("Summation is %.2f\n", n1 + n2 + n3 + n4);
    printf("Average is %.3f",(n1 + n2 + n3 + n4)/4);
    return 0;
}