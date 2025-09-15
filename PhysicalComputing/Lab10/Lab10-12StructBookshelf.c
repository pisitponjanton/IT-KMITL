#include <stdio.h>
#include <string.h>

struct Book
{
    char id[10];
    char name[100];
    char author[100];
};

int main()
{
    int n;
    char id[10];
    scanf("%d %s", &n, id);
    struct Book book[n];

    for (int i = 0; i < n; i++)
    {
        scanf(" %s", book[i].id);
        scanf(" %s", book[i].name);
        scanf(" %s", book[i].author);
    }

    for (int i = 0; i < n; i++)
    {
        if (strcmp(id, book[i].id) == 0)
        {
            printf("%s %s %s", book[i].id, book[i].name, book[i].author);
            return 0;
        }
    }
    
    printf("Not Found");

    return 0;
}
