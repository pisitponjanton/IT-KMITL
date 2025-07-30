#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);

    if (n == 0)
    {
        printf("Duck Type: Silent Duck");
    }
    else if (n >= 1 && n <= 10)
    {
        printf("Duck Type: Chill Duck");
    }
    else if (n >= 11 && n <= 50)
    {
        printf("Duck Type: Happy Duck");
    }
    else if (n > 50)
    {
        printf("Duck Type: Talkative Duck");
    }
    else{
        printf("Error");
    }
    return 0;
}