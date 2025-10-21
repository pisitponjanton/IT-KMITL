#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

int check_char(char x, char *list, int size);
void bbsort(char *list, int size);
void countchar(char str[], char *list, int *numlist, int size);

int main()
{
    char str[255];
    int n = 0;

    int size_p = 0;
    char *p;
    p = (char *)malloc(255 * sizeof(char));

    int *d;
    d = (int *)malloc(255 * sizeof(int));

    scanf("%[^\n]", str);
    for (int i = 0; str[i] != '\0'; i++)
    {
        if (isalpha(str[i]) && !check_char(str[i], p, size_p))
        {
            *(p + size_p) = str[i];
            size_p++;
        }
    }

    bbsort(p, size_p);
    countchar(str, p, d, size_p);

    for (int i = 0; i < size_p; i++)
    {
        printf("%c = %d\n", *(p + i), *(d + i));
    }

    free(p);
    free(d);
    return 0;
}

int check_char(char x, char *list, int size)
{
    for (int i = 0; i < size; i++)
    {
        if (*(list + i) == x)
        {
            return 1;
        }
    }
    return 0;
}

void bbsort(char *list, int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            char b = *(list + i);
            char n = *(list + j);

            char bl = tolower(b);
            char nl = tolower(n);

            if (bl < nl || (bl == nl && b > n))
            {
                char pv = *(list + i);
                *(list + i) = *(list + j);
                *(list + j) = pv;
            }
        }
    }
}

void countchar(char str[], char *list, int *numlist, int size)
{
    for (int i = 0; i < size; i++)
    {
        int count = 0;
        for (int j = 0; str[j] != '\0'; j++)
        {
            if (*(list + i) == str[j])
            {
                count++;
            }
        }
        *(numlist + i) = count;
    }
}