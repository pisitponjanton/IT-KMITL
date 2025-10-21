#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void sortlist(int n, int *p)
{
    for (int i = 0; i < n - 1; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (*(p + i) >= *(p + j))
            {
                int q = *(p + i);
                *(p + i) = *(p + j);
                *(p + j) = q;
            }
        }
    }
}

int main()
{
    char hway[4][100] = {
        "Phet Kasem\0",
        "Phahonyothin\0",
        "Sukhumvit\0",
        "Mittraphap\0",
    };

    int n;
    scanf("%d", &n);
    int *list_int = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++)
    {
        char *text = (char *)malloc(100 * sizeof(char));
        scanf(" %[^\n]", text);
        for (int j = 0; j < 4; j++)
        {
            if (strcmp(hway[j], text) == 0)
            {
                *(list_int + i) = j;
                break;
            }
        }
        free(text);
    }

    sortlist(n, list_int);

    for (int i = 0; i < n; i++)
    {
        printf("%s\n", hway[*(list_int + i)]);
    }

    free(list_int);
    return 0;
}
