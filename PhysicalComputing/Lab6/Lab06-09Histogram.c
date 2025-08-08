#include <stdio.h>
#include <ctype.h>

int check(int num, char x, char l[]);
int count(int num, char x, char l[]);

int main()
{
    int num, n_nomore = 0;
    scanf("%d", &num);
    char c[num], nomore[num];

    for (int i = 0; i < num; i++)
    {
        scanf(" %c", &c[i]);
        c[i] = tolower(c[i]);
    }

    for (int i = 0; i < num; i++)
    {
        if (check(n_nomore, c[i], nomore))
        {
            nomore[n_nomore] = c[i];
            n_nomore++;
        }
    }

    for (int i = 0; i < n_nomore; i++)
    {
        printf("%c: %d\n", nomore[i], count(num, nomore[i], c));
    }

    return 0;
}

int check(int num, char x, char l[])
{
    for (int i = 0; i < num; i++)
    {
        if (x == l[i])
            return 0;
    }
    return 1;
}

int count(int num, char x, char l[])
{
    int sum = 0;
    for (int i = 0; i < num; i++)
    {
        if (x == l[i])
            sum ++;
    }
    return sum;
}