#include <stdio.h>

int main()
{
    char TEXT[101];
    int i = 0;
    while (i < 100)
    {
        scanf("%[^\n]s", &TEXT[i]);
        if(TEXT[i] == '\0'){
            break;
        }
        i++;
    }

    for (int j = i-1; j >= 0; j--)
    {
        printf("%c", TEXT[j]);
    }
    return 0;
}