#include <stdio.h>

int main()
{
    int n;
    double b = 2800.0;
    double sum = 0;
    scanf("%d", &n);

    for (int i = 1; i <= n/2; i++)
    {
        sum += b * 2.0 / 100.0;
        b -= b * 2.0 / 100.0;
    }

    printf("%.2lf\n", sum);
    if(2800.0*70.0/100.0 <= b){
        printf("Safe");
    }else{
        printf("Danger");
    }

    return 0;
}