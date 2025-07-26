#include <stdio.h>

int main()
{
    char info[40];
    int g1, g2, g3, g4, g5, g6;
    scanf("%[^\n]s", info);
    scanf("%d %d %d %d %d %d", &g1, &g2, &g3, &g4, &g5, &g6);

    float gpa = (g1 + g2 + g3 + g4 + g5 + g6) / 6.00f;

    printf("Grade announcement 1/2568: %s\n", info);
    printf("GPS/GPA: %.2f\n", gpa);
    return 0;
}
