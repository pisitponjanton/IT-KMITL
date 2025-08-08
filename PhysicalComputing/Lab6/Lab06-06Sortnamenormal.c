#include <stdio.h>
#include <ctype.h>

int x_more_y(char x[], char y[]);
void swap(char a[], char b[]);

int main()
{
    char TEXT[20][60];
    int j = 0;
    for (int i = 0; i < 20; i++)
    {
        scanf(" %[^\n]", TEXT[i]);
    }

    for (int i = 0; i < 20; i++)
    {
        for (int j = 0; TEXT[i][j] != '\0'; j++)
        {
            if (j == 0 || TEXT[i][j-1] == ' ')
            {
                TEXT[i][j] = toupper(TEXT[i][j]);
            }
            else
            {
                TEXT[i][j] = tolower(TEXT[i][j]);
            }
        }
    }

    for (int i = 0; i < 19; i++)
    {
        for (int j = 0; j < 19 - i; j++)
        {
            if (x_more_y(TEXT[j], TEXT[j + 1]))
            {
                swap(TEXT[j], TEXT[j + 1]);
            }
        }
    }

    for (int i = 0; i < 20; i++)
    {
        printf("%s\n", TEXT[i]);
    }

    return 0;
}

int x_more_y(char x[], char y[])
{
    int i = 0;
    while (x[i] != '\0' && y[i] != '\0')
    {
        if (x[i] > y[i])
            return 1;
        if (x[i] < y[i])
            return 0;
        i++;
    }
    if (x[i] != '\0')
        return 1;
    return 0;
}

void swap(char a[], char b[])
{
    char temp;
    for (int i = 0; i < 60; i++)
    {
        temp = a[i];
        a[i] = b[i];
        b[i] = temp;

        if (a[i] == '\0' && b[i] == '\0')
            break;
    }
}