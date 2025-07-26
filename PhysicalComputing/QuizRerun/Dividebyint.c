# include <stdio.h>

int main()
{
    int a, b;
    scanf("%d %d",&a ,&b);
    float h = ((float)a)/b;

    printf("%.2f", h);
    return 0;
}