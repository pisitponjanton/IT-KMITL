#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node
{
    char *data;
    int index;
    struct Node *next;
} Node;

typedef struct LinkList
{
    unsigned int count;
    Node *head;
} LinkList;

LinkList *createLinkList();
Node *createNode(char *data, int index);
void insert(LinkList *list, char *data);
void findIndex(LinkList *list, int Index);

LinkList *createLinkList()
{
    LinkList *newList = (LinkList *)malloc(sizeof(LinkList));
    newList->count = 0;
    newList->head = NULL;

    return newList;
}

Node *createNode(char *data, int index)
{
    Node *newNode = (Node *)malloc(sizeof(Node));

    newNode->data = (char *)malloc(strlen(data) + 1);
    strcpy(newNode->data, data);

    newNode->index = index;
    newNode->next = NULL;

    return newNode;
}

void insert(LinkList *list, char *data)
{
    if (list->count == 0)
    {
        Node *pNew = createNode(data, list->count);
        list->head = pNew;
    }
    else
    {
        Node *pointer = list->head;
        while (pointer->next != NULL)
        {
            pointer = pointer->next;
        }
        Node *pNew = createNode(data, list->count);
        pointer->next = pNew;
    }

    list->count++;
}

void findIndex(LinkList *list, int index)
{
    int len = list->count;
    Node *pointer = list->head;
    while (pointer != NULL)
    {
        if (pointer->index == index || pointer->index - len == index)
        {
            printf("%s", pointer->data);
            return;
        }
        pointer = pointer->next;
    }
    printf("Error");
}

int main()
{
    int index;
    LinkList *list = createLinkList();
    while (1)
    {
        char *line = (char *)malloc(21 * sizeof(char));
        scanf(" %s", line);

        if (strcmp(line, "Last") == 0)
        {
            free(line);
            break;
        }

        insert(list, line);
    }
    scanf(" %d", &index);
    findIndex(list, index);

    Node *current = list->head;
    while (current != NULL)
    {
        free(current->data);
        Node *temp = current;
        current = current->next;
        free(temp);
    }
    free(list);
    return 0;
}
