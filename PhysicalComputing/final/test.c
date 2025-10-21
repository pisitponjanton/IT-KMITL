#include <stdio.h>
int main(){
    int a = 3, *b, **c;
    b = &a;
    c = &b;

    printf("%d\n", *b);
    printf("%p", &(*c));
}