#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char *type = (char *)malloc(4 * sizeof(char));
    int a, b, c, d, e;
    scanf("%[^\n]", type);
    scanf(" %d %d %d %d %d", &a, &b, &c, &d, &e);

    if (strcmp(type, "MAX") == 0)
    {
        int max = a;
        if (b > max)
            max = b;
        if (c > max)
            max = c;
        if (d > max)
            max = d;
        if (e > max)
            max = e;
        printf("MAX : %d", max);
    }
    else
    {
        int min = a;
        if (b < min)
            min = b;
        if (c < min)
            min = c;
        if (d < min)
            min = d;
        if (e < min)
            min = e;
        printf("MIN : %d", min);
    }

    return 0;
}