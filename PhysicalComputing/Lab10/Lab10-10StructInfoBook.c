#include <stdio.h>

typedef struct
{
    char name[61];
    char surname[61];
    char sex[10];
    int age;
    char id[13];
    float gpa;
} Student_info;

int main()
{
    Student_info student1;
    scanf(" %s", student1.name);
    scanf(" %s", student1.surname);
    scanf(" %s", student1.sex);
    scanf(" %d", &student1.age);
    scanf(" %s", student1.id);
    scanf(" %f", &student1.gpa);

    if (student1.sex[0] == 'M')
    {
        printf("Mr %c %s (%d) ID: %s GPA %.2f", student1.name[0], student1.surname, student1.age, student1.id, student1.gpa);
    }
    else
    {
        printf("Miss %c %s (%d) ID: %s GPA %.2f", student1.name[0], student1.surname, student1.age, student1.id, student1.gpa);
    }

    return 0;
}