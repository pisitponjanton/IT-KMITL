#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

typedef struct
{
    char name[61];
    char surname[61];
    char sex[10];
    int age;
    char id[13];
    float gpa;
} Student_info;

void input(Student_info *s);
void print(Student_info *s);
int types(char type[], Student_info *s1, Student_info *s2);
void sort(Student_info student[], char type[]);

int main()
{
    Student_info *student = (Student_info *)malloc(20 * sizeof(Student_info));

    for (int i = 0; i < 20; i++)
    {
        input(&student[i]);
    }

    char type[10];
    scanf("%s", type);
    sort(student, type);

    for (int i = 0; i < 20; i++)
    {
        print(&student[i]);
    }

    free(student);

    return 0;
}

void input(Student_info *s)
{
    scanf(" %s", s->name);
    scanf(" %s", s->surname);
    scanf(" %s", s->sex);
    scanf(" %d", &s->age);
    scanf(" %s", s->id);
    scanf(" %f", &s->gpa);
}

void print(Student_info *s)
{
    if (strcmp(s->sex, "Male") == 0)
    {
        printf("Mr %c %s (%d) ID: %s GPA %.2f\n", s->name[0], s->surname, s->age, s->id, s->gpa);
    }
    else
    {
        printf("Miss %c %s (%d) ID: %s GPA %.2f\n", s->name[0], s->surname, s->age, s->id, s->gpa);
    }
}

void sort(Student_info student[], char type[])
{
    for (int i = 0; i < 20; i++)
    {
        for (int j = i + 1; j < 20; j++)
        {
            if (types(type, &student[i], &student[j]))
            {
                Student_info studenttest = student[i];
                student[i] = student[j];
                student[j] = studenttest;
            }
        }
    }
}

int types(char type[], Student_info *s1, Student_info *s2)
{
    if (tolower(type[0]) == 'n')
    {
        return strcmp(s1->name, s2->name) > 0;
    }
    else if (tolower(type[0]) == 's')
    {
        return strcmp(s1->surname, s2->surname) > 0;
    }
    else
    {
        return strcmp(s1->id, s2->id) > 0;
    }
}
