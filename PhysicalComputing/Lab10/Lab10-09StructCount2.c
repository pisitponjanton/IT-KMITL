#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct TEXT
{
    char text[451];
};
int words(char x[]);
int chars(char x[]);

int main()
{
    int indexList = 0;
    int capacity = 10;
    struct TEXT *list = (struct TEXT *)malloc(capacity * sizeof(struct TEXT));

    while (1)
    {
        char str[451];
        scanf(" %[^\n]", str);
        if (str[0] == '.')
            break;

        if (indexList >= capacity)
        {
            list = (struct TEXT *)realloc(list, (capacity * 2) * sizeof(struct TEXT));
        }

        strcpy(list[indexList].text, str);
        indexList++;
    }

    int allWords = 0, allChars = 0;
    for (int i = 0; i < indexList; i++)
    {
        allWords += words(list[i].text);
        allChars += chars(list[i].text);
    }

    printf("Char = %d, word = %d, line = %d", allChars, allWords, indexList);

    free(list);
    return 0;
}

int words(char x[])
{
    int word = 0;
    for (int i = 0;; i++)
    {
        if (x[i] == ' ' || x[i] == '\0')
        {
            word++;
            if (x[i] == '\0')
            {
                break;
            }
        }
    }

    return word;
}

int chars(char x[])
{
    int chs = 0;
    for (int i = 0; x[i] != '\0'; i++)
    {
        if (x[i] != ' ')
        {
            chs++;
        }
    }

    return chs;
}