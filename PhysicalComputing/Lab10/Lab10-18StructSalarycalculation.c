#include <stdio.h>
#include <string.h>

typedef struct Record
{
    char id[10];
    char name[100];
    long salary;
    long sales;
} Record;

int main()
{
    int n;
    char id[10];
    scanf("%d", &n);
    Record record[n];
    for (int i = 0; i < n; i++)
    {
        scanf(" %s", record[i].id);
        scanf(" %s", record[i].name);
        scanf(" %ld", &record[i].salary);
        scanf(" %ld", &record[i].sales);
    }
    scanf(" %s", id);

    for (int i = 0; i < n; i++)
    {
        if (strcmp(id, record[i].id) == 0)
        {
            double commission = record[i].sales * 2.0 / 100.0;
            printf("%s\n", record[i].id);
            printf("%s\n", record[i].name);
            printf("%ld\n", record[i].sales);
            printf("%.2lf\n", commission);
            printf("%ld\n", record[i].salary);
            printf("%.2lf\n", record[i].salary + commission);
            return 0;
        }
    }

    printf("ID not found !!!");

    return 0;
}