#include "stdio.h"

int getNum(void);
int sqr(int x);
int printOne(int x);

int main() {
    int a;
    int b;
    a = getNum();
    b = sqr(a);
    printOne(b);
    return 0;
}

int getNum(void) {
    int numIn;
    scanf("%d", &numIn);
    return numIn;
}

int sqr(int x) {
    return x * x;
}

int printOne(int x) {
    printf("The value is: %d\n", x);
    return 0;
}
