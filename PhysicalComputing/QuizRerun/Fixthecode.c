#include <stdio.h>

int main()
{
    int celsius;
    scanf("%d", &celsius);

    float fahrenheit = (celsius * 9.0 / 5) + 32;

    printf("%.1f\n", fahrenheit);
    return 0;
}