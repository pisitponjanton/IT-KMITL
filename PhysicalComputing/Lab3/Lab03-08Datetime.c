#include <stdio.h>

int main()
{
    int time;
    scanf("%d", &time);
    int d = (time / 86400);
    int h = (time / 3600) % 24;
    int m = (time / 60) % 60;
    int s = time % 60;
    printf("%d s = %d d %d h %d m %d s", time, d, h, m, s);
    return 0;
}