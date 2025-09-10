# include <stdio.h>

int main()
{
    char str[200];

    scanf("%[^\n]", str);

    char st[] = {str[0],'.',' ','.','\0'};

    for(int i = 0; str[i] != '\0'; i++){
        if(str[i-1] == ' '){
            st[2] = str[i];
        }
    }

    printf("%s", st);

    return 0;
}