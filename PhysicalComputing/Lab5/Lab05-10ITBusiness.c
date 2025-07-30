#include <stdio.h>

int main()
{
    float in, out;
    int count = 0;
    scanf("%f %f", &in, &out);

    while (1)
    {
        char a;
        float b;
        scanf("%c %f", &a, &b);
        if (a == 'E' || count == 3)
        {
            break;
        }

        if (a == 'D')
        {
            if (out >= b)
            {
                in += b;
                out -= b;
                count = 0;
            }
            else
            {
                ++count;
            }
        }
        
        if (a == 'W')
        {
            if (in >= b)
            {
                in -= b;
                out += b;
                count = 0;
            }
            else
            {
                ++count;
            }
        }
    }

    printf("%.2f\n", in);
    printf("%.2f", out);
    return 0;
}