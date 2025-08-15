#include <stdio.h>
#include <ctype.h>

void change(char x[]);
int is_Same(char x[], char y[]);

int main()
{
    char x[101], y[101];
    scanf(" %[^\n]", x);
    scanf(" %[^\n]", y);

    change(x);
    change(y);

    printf("*** Results ***\n");
    printf("%s\n", x);
    printf("%s\n", y);
    printf("***************\n");
    printf("Both strings are%sthe same.", is_Same(x,y) ? " " : " not ");

    return 0;
}

int is_Same(char x[], char y[])
{
    int n_x = 0, n_y = 0;
    for (int i = 0; x[i] != '\0'; i++)
    {
        n_x++;
    }
    for (int i = 0; y[i] != '\0'; i++)
    {
        n_y++;
    }

    if (n_x != n_y)
    {
        return 0;
    }
    else
    {
        for (int i = 0; i < n_x; i++)
        {
            if (tolower(x[i]) != tolower(y[i]))
            {
                return 0;
            }
        }
    }

    return 1;
}

void change(char x[])
{
    for (int i = 0; x[i] != '\0'; i++)
    {
        if (islower(x[i]))
        {
            x[i] = toupper(x[i]);
        }
        else
        {
            x[i] = tolower(x[i]);
        }
    }
}