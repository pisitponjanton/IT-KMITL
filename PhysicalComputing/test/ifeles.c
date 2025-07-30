#include <stdio.h>

int main(){
    char info[255];
    int num;
    scanf("%[^\n]", info);
    scanf("%d", &num);
    printf("%s\n", info);
    printf("%d", num);
    return 0;
}