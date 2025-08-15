#include <stdio.h>
#include <ctype.h>

void change(char x[]);
int checkXtoY(char x[], char y[]);
void switchXtoY(char x[], char y[]);

int main()
{
    int n;
    scanf("%d", &n);

    char NAME[n][255];
    for (int i = 0; i < n; i++)
    {
        scanf(" %[^\n]", NAME[i]);
        change(NAME[i]);
    }

    // Selection sort
    for (int i = 0; i < n - 1; i++)
    {
        int min_idx = i;
        for (int j = i + 1; j < n; j++)
        {
            if (checkXtoY(NAME[min_idx], NAME[j]))
            {
                min_idx = j;
            }
        }
        if (min_idx != i)
        {
            switchXtoY(NAME[i], NAME[min_idx]);
        }
    }

    for (int i = 0; i < n; i++)
    {
        printf("%s\n", NAME[i]);
    }

    return 0;
}

void change(char x[])
{
    for (int i = 0; x[i] != '\0'; i++)
    {
        if (i == 0 || x[i - 1] == ' ')
            x[i] = toupper((unsigned char)x[i]);
        else
            x[i] = tolower((unsigned char)x[i]);
    }
}

int checkXtoY(char x[], char y[])
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

void switchXtoY(char x[], char y[])
{
    char temp;
    int i = 0;
    while (1)
    {
        temp = x[i];
        x[i] = y[i];
        y[i] = temp;
        if (x[i] == '\0' && y[i] == '\0')
            break;
        i++;
    }
}
