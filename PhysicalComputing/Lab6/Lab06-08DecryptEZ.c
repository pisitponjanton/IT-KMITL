#include <stdio.h>
#include <ctype.h>

char L[] = {
    'A', 'B', 'X', 'Y', 'P',
    'Q', 'R', 'M', 'N', 'C', 
    'E', 'D', 'K', 'L', 'J', 
    'O', 'S', 'H', 'T', 'U', 'F', 
    'V', 'Z', 'G', 'W', 'I'};

char encrypt(char x);

int main()
{
    char text[200];
    scanf("%[^\n]", text);

    for (int i = 0; text[i] != '\0'; i++)
    {
        text[i] = encrypt(text[i]);
    }

    printf("%s", text);
    return 0;
}

char encrypt(char x)
{
    char y = x;
    for (int i = 0; i < 26; i++)
    {
        if (L[i] == toupper(x) && i <= 20)
        {
            y = L[i + 5];
        }
        else if (L[i] == toupper(x) && i > 20)
        {
            y = L[i - 21];
        }
    }
    if (islower(x))
    {
        y = tolower(y);
    }
    return y;
}