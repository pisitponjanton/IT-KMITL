#include <stdio.h>

int main()
{
    char fname1[30], lname1[30];
    char fname2[30], lname2[30];
    char fname3[30], lname3[30];

    scanf("%s", fname1);
    scanf("%s", lname1);
    scanf("%s %s", fname2, lname2);
    scanf("%s %s", fname3, lname3);

    printf("Person 1: %s %s\n", fname1, lname1);
    printf("Person 2: %s %s\n", fname2, lname2);
    printf("Person 3: %s %s\n", fname3, lname3);

    return 0;
}
