#include <stdio.h>

int main(){
    double price;
    int sell,n;
    scanf("%lf", &price);
    scanf("%d", &sell);
    scanf("%d", &n);

    double p1 = (n*price) * (100-sell)/100;
    double p2 = ((n/3) * price * 2) + n%3 * price ;

    if (p1 <= p2){
        printf("Discount %d%%\n", sell);
        printf("%.2lf\n",p1);
    }else{
        printf("Buy 2 Get 1\n");
        printf("%.2lf\n",p2);
    }
    
    return 0;
}