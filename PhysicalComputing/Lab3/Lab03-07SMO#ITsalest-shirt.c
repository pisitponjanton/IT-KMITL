# include <stdio.h>

int main(){
    double raka, p, n;
    scanf("%lf", &raka);
    scanf("%lf", &p);
    scanf("%lf", &n);
    printf("%.2lf", (raka*(100-p)/100) * n);
    return 0;
}