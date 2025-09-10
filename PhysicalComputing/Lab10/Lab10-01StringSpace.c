# include <stdio.h>

int main()
{
    char text[150];

    scanf("%[^\n]", text);

    for(int i = 0; text[i] != '\0'; i++){
        if(text[i] != ' '){
            printf("%c",text[i]);
        }
    }

    return 0;
}