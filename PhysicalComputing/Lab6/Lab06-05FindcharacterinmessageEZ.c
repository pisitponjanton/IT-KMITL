#include <stdio.h>
#include <ctype.h>

int main()
{
    char TEXT[301], text;
    int NUM[300], num = 0, j = 0;

    scanf(" %[^\n]", TEXT);

    scanf(" %c", &text);

    for (int i = 0; TEXT[i] != '\0'; i++)
    {
        if (tolower(TEXT[i]) == text)
        {
            NUM[num] = i + 1;
            num++;
        }
    }

    if (num > 0)
    {
        printf("There is/are %d \"%c\" in the above sentences.\n", num, text);
        printf("Position: ");
        for (int i = 0; i < num; i++)
        {
            if (i != num - 1)
            {
                printf("%d, ", NUM[i]);
            }
            else
            {
                printf("%d", NUM[i]);
            }
        }
    }
    else
    {
        printf("Not found.");
    }

    return 0;
}