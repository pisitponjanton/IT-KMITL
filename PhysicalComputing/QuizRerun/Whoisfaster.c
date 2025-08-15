#include <stdio.h>

void getDay(int x[]);
int sumDay(int x[]);

int main()
{
    char t1[255], t2[255];
    int d1[7], d2[7];
    scanf(" %[^\n]", t1);
    getDay(d1);
    scanf(" %[^\n]", t2);
    getDay(d2);

    int m1 = sumDay(d1);
    int m2 = sumDay(d2);

    int w1 = 0, w2 = 0, ww = 0;
    for (int i = 0; i < 7; i++)
    {
        if (d1[i] > d2[i])
        {
            w1++;
        }
        else if (d1[i] < d2[i])
        {
            w2++;
        }
        else
        {
            ww++;
        }
    }

    printf("%s: %d minutes, average %d minutes/day\n", t1, m1, m1 / 7);
    printf("%s: %d minutes, average %d minutes/day\n", t2, m2, m2 / 7);
    printf("Faster days - %s: %d, %s: %d, Equal: %d", t1, w2, t2, w1, ww);

    return 0;
}

void getDay(int x[])
{
    for (int i = 0; i < 7; i++)
    {
        scanf("%d", &x[i]);
    }
}

int sumDay(int x[])
{
    int sum = 0, avg = 0;
    for (int i = 0; i < 7; i++)
    {
        sum += x[i];
    }

    return sum;
}
