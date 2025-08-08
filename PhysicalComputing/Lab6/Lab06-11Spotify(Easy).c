#include <stdio.h>

int main()
{
    long time_M, time_can_use;
    int time_S, song_N;

    scanf(" %ld . %d", &time_M, &time_S);
    scanf(" %d", &song_N);
    char Q[song_N][50];
    long T[song_N];
    time_can_use = time_M * 60 + time_S;

    for (int i = 0; i < song_N; i++)
    {
        char song_Name[50];
        int queue;
        long m;
        int s;
        int time_S, song_N;
        scanf(" Queue#%d <|>", &queue);
        scanf(" %[^<]", Q[queue - 1]);
        scanf(" <|>");
        scanf(" %ld . %d", &m, &s);
        T[queue - 1] = m * 60 + s;
    }

    long sum_time = 0;
    for (int i = 0; i < song_N; i++)
    {
        sum_time += T[i];
    }
    time_can_use %= sum_time;

    int num = 0;

    if (time_can_use == 0)
    {
        num = song_N - 1;
    }

    while (time_can_use > 0)
    {
        for (int i = 0; i < song_N; i++)
        {
            if (time_can_use <= 0)
            {
                break;
            }

            time_can_use -= T[i];
            num = i;
        }
    }

    double p = (((double)(time_can_use + T[num]) / T[num]) * 100);
    int p_new;
    if (p > 0 && p < 1)
    {
        p_new = 1;
    }
    else
    {
        p_new = (int)p;
    }

    printf("Song Order: %d\n", num + 1);
    printf("Song Name: %s\n", Q[num]);
    if (p_new == 100)
        printf("Song Process: Complete");
    else
        printf("Song Process: %d%%", p_new);

    return 0;
}