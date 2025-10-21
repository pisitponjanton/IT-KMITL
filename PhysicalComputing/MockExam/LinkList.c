#include <stdio.h>
#include <stdlib.h>

typedef struct LinkList
{
    struct Node *head;
    unsigned int size;
} LinkList;

typedef struct Node
{
    int data;
    struct Node *next;
} Node;

LinkList *createLinkList()
{
    LinkList *newList = (LinkList *)malloc(sizeof(LinkList));
    newList->head = NULL;
    newList->size = 0;

    return newList;
}

Node *createNode(int data)
{
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->next = NULL;
    newNode->data = data;

    return newNode;
}

void addData(int data, LinkList *list)
{
    Node *newnode = createNode(data);
    Node *pev = list->head;
    if (pev == NULL)
    {
        list->head = newnode;
        list->size += 1;
    }
    else
    {
        while (pev->next != NULL)
        {
            pev = pev->next;
        }
        pev->next = newnode;
    }
}

void insertData(int index, LinkList *list, int data)
{
    Node *newNode = createNode(data);
    if (index == 0 || list->head == NULL)
    {
        newNode->next = list->head;
        list->head = newNode;
        return;
    }

    Node *pev = list->head;
    int count = 0;

    while (pev != NULL && count < index - 1)
    {
        pev = pev->next;
        count++;
    }

    if (pev != NULL)
    {
        newNode->next = pev->next;
        pev->next = newNode;
    }
}

void printList(LinkList *list)
{
    Node *pv = list->head;
    while (pv != NULL)
    {
        printf("%d ", pv->data);
        pv = pv->next;
    }
}

int main()
{
    int n;
    scanf("%d", &n);
    LinkList *list = createLinkList();
    for (int i = 0; i < n; i++)
    {
        int data;
        scanf(" %d", &data);
        addData(data, list);
    }
    int index, indata;
    scanf(" %d", &index);
    scanf(" %d", &indata);
    insertData(index, list, indata);
    printList(list);
}