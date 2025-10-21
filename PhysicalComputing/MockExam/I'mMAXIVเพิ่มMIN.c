#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    char mm[10];
    int size = 5;
    int *num = (int *)malloc(size * sizeof(int));
    scanf("%[^\n]", mm);

    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &(*(num + i)));
    }

    if (strcmp("MAX", mm) == 0)
    {
        int max = *num;
        for (int i = 0; i < 5; i++)
        {
            if (max < *(num + i))
            {
                max = *(num + i);
            }
        }
        printf("MAX : %d", max);
        return 0;
    }

    if (strcmp("MIN", mm) == 0)
    {
        int min = *num;
        for (int i = 0; i < 5; i++)
        {
            if (min > *(num + i))
            {
                min = *(num + i);
            }
        }
        printf("MIN : %d", min);
        return 0;
    }

    return 0;
}