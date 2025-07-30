#include <stdio.h>

int main()
{
    int n, sum;
    while (n != -9)
    {
        scanf("%d", &n);
        if(n == -9){
            break;
        }
        sum += n;
    }
    printf("%d", sum);
    return 0;
}