#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int checkList(char *list, char txt, int *num, int size);
void sort(int size, char *list, int *num);

int main()
{
    int size = 0;
    char *txt = (char *)malloc(255 * sizeof(char));
    scanf("%[^\n]", txt);

    char *list = (char *)malloc(255 * sizeof(char));
    int *num = (int *)malloc(255 * sizeof(int));
    for (int i = 0; *(txt + i) != '\0'; i++)
    {
        if (!checkList(list, *(txt + i), num, size) && isalpha(*(txt + i)))
        {
            *(list + size) = *(txt + i);
            size++;
        }
    }

    sort(size, list, num);

    for (int i = 0; *(list + i) != '\0'; i++)
    {
        printf("%c = %d\n", *(list + i), *(num + i));
    }

    return 0;
}

int checkList(char *list, char txt, int *num, int size)
{
    for (int i = 0; *(list + i) != '\0'; i++)
    {
        if (txt == *(list + i))
        {
            *(num + i) += 1;
            return 1;
        }
    }
    *(num + size) = 1;
    return 0;
}

void sort(int size, char *list, int *num)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            char f = *(list + i);
            char r = *(list + j);

            char lf = tolower(*(list + i));
            char lr = tolower(*(list + j));
            if (lf < lr || ( f > r && lf == lr))
            {
                char p = *(list + i);
                *(list + i) = *(list + j);
                *(list + j) = p;

                int pn = *(num + i);
                *(num + i) = *(num + j);
                *(num + j) = pn;
            }
        }
    }
}