#include <stdio.h>

int main()
{
    char fname[30], lname[30], id[8];
    int DD, MM, YYYY;
    float gpa;

    scanf("%s", fname);
    scanf("%s", lname);
    scanf("%s", id);
    scanf("%d/%d/%d", &DD, &MM, &YYYY);
    scanf("%f", &gpa);

    printf("Fullname: %s %s\n", fname, lname);
    printf("ID: %s\n", id);
    printf("DOB: %02d-%02d-%04d\n", DD, MM, YYYY);
    printf("GPA: %.2f\n", gpa);

    return 0;
}
