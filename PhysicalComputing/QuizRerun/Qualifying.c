#include <stdio.h>

int main()
{
    float s1, s2, s3, s;
    int n = 1;
    char n1[35], n2[35], n3[35];
    scanf("%f %[^\n]s", &s1, n1);
    scanf("%f %[^\n]s", &s2, n2);
    scanf("%f %[^\n]s", &s3, n3);
    s = s1;

    if (s2 < s)
    {
        s = s2;
        n = 2;
    }
    if (s3 < s)
    {
        s = s3;
        n = 3;
    }
    if (n == 1)
    {
        printf("%s is Fastest : %.3f", n1, s);
    }
    if (n == 2)
    {
        printf("%s is Fastest : %.3f", n2, s);
    }
    if (n == 3)
    {
        printf("%s is Fastest : %.3f", n3, s);
    }
    return 0;
}