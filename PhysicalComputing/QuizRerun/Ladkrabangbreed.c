#include <stdio.h>
#include <math.h>

int main()
{
    int n;
    char name1[50], name2[50], name3[50];
    scanf("%d", &n);
    scanf("%s %s %s", name1, name2, name3);

    double n1, n2, n3;
    double sum1 = 0.0, sum2 = 0.0, sum3 = 0.0;

    for (int i = 0; i < n; i++)
    {
        scanf("%lf %lf %lf", &n1, &n2, &n3);
        sum1 += n1;
        sum2 += n2;
        sum3 += n3;
    }

    int d1 = (int)ceil(sum1 / (name1[0] == 'N' ? 6.6 : 5.5));
    int d2 = (int)ceil(sum2 / (name2[0] == 'N' ? 6.6 : 5.5));
    int d3 = (int)ceil(sum3 / (name3[0] == 'N' ? 6.6 : 5.5));

    printf("%s: %d refills\n", name1, d1);
    printf("%s: %d refills\n", name2, d2);
    printf("%s: %d refills\n", name3, d3);

    return 0;
}
