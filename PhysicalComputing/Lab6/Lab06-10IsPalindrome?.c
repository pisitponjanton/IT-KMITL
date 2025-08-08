#include <stdio.h>

int main()
{
    char text[100], n = 0;
    scanf("%[^\n]", text);

    for (int i = 0; text[i] != '\0'; i++)
    {
        ++n;
    }

    char retext[n];
    for(int i = n; i >= 0; i--){
        retext[n-i] = text[i-1];
    }

    for(int i = 0; i< n; i++){
        if(text[i] != retext[i]){
            printf("It is not Palindrome.");
            return 0;
        }
    }

    printf("It is Palindrome.");

    return 0;
}