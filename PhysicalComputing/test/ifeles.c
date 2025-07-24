#include <stdio.h>

int main(){
    int a;
    float b;
    char c;

    scanf(" %d", &a);
    scanf(" %f", &b);
    scanf(" %c", &c);

    printf("%.2lf\n", (float) a);
    printf("%d\n", (int) b);
    printf("%d\n", c);

    return 0;
}