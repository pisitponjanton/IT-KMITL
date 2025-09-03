#include <stdio.h>
void sort(int NUM[], int n);
int main()
{
    int n;
    scanf(" %d", &n);

    int NUM[n];
    for (int i = 0; i < n; i++)
    {
        scanf(" %d", &NUM[i]);
    }

    sort(NUM, n);

    for (int i = 0; i < n; i++)
    {
        printf("%d ", NUM[i]);
    }

    return 0;
}

void sort(int NUM[], int n)
{
    for (int i = 0; i < n; i++)
    {
        int min = NUM[i];
        int minIndex = i;

        for (int j = i + 1; j < n; j++)
        {
            if (min >= NUM[j])
            {
                min = NUM[j];
                minIndex = j;
            }
        }

        NUM[minIndex] = NUM[i];
        NUM[i] = min;
    }
}
