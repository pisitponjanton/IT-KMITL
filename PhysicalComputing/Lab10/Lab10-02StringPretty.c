# include <stdio.h>
# include <string.h>
# include <math.h>

void start(int x);
void centers(int x,char str[]);

int main()
{
    int NUM;
    char str1[50],str2[40];

    scanf(" %d", &NUM);
    scanf(" %[^\n]", str1);
    scanf(" %[^\n]", str2);

    start(NUM);
    centers(NUM, str1);
    centers(NUM, str2);
    start(NUM);

    return 0;
}

void start(int x){
    for(int i = 0; i < x; i++){
        printf("*");
    }
    printf("\n");
}

void centers(int x,char str[]){
    printf("*");
    float t = ((x-2) - strlen(str))/ 2.0;
    int c = ceil(t);
    int target = x - c - strlen(str);
    for(int i = 0; i < c; i++){
        printf(" ");
    }
    printf("%s", str);
    for(int i = 0; i < target-2; i++){
        printf(" ");
    }
    printf("*\n");
}