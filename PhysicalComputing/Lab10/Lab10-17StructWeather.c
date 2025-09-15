#include <stdio.h>
#include <string.h>

typedef struct Weather
{
    char outlook[9]; // outlook{overcast,sunny,rain}
    int temperature;
    int humidity;
    char wind; // wind{T,F}
} Weather;

int main()
{
    int n;
    scanf("%d", &n);

    Weather weather[n];
    for (int i = 0; i < n; i++)
    {
        scanf(" %s", weather[i].outlook);
        scanf(" %d", &weather[i].temperature);
        scanf(" %d", &weather[i].humidity);
        scanf(" %c", &weather[i].wind);
    }

    for (int i = 0; i < n; i++)
    {
        if (strcmp(weather[i].outlook, "overcast") == 0)
            printf("yes\n");
        else if (strcmp(weather[i].outlook, "rain") == 0)
        {
            if (weather[i].wind == 'F')
                printf("yes\n");
            else
                printf("no\n");
        }
        else
        {
            if (weather[i].humidity > 77.5)
                printf("no\n");
            else
                printf("yes\n");
        }
    }

    return 0;
}