# include <stdio.h>
# include <ctype.h>

int main()
{
    char c;
    char str[150];
    int num = 0;

    scanf("%c", &c);
    scanf(" %[^\n]", str);

    for(int i = 0; str[i] != '\0'; i++)
    {
        if(tolower(str[i]) == tolower(c)){
            num++;
        }
    }

    printf("%d", num);

    return 0;
}