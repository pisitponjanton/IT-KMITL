#include <stdio.h>

void sort(char x[]);

int main()
{
    char str[200];
    scanf("%[^\n]", str);
    sort(str);
    printf("%s", str);
    return 0;
}

void sort(char x[])
{
    for(int i = 0; x[i] != '\0'; i++){
        for(int j = i+1; x[j] != '\0'; j++)
            if(x[i] > x[j]){
                char s = x[i];
                x[i] = x[j];
                x[j] = s;
            }
    }
}