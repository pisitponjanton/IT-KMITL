#include <stdio.h>

int main()
{
    double M[3][3];
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            scanf("%lf", &M[i][j]);
        }
    }
    if (M[0][1] == 0.0 && M[0][2] == 0.0 && M[1][0] == 0.0 && M[1][2] == 0.0 && M[2][0] == 0.0 && M[2][1] == 0.0)
    {
        if(M[0][0] == M[1][1] && M[1][1] == M[2][2] && M[0][0] == M[2][2]){
            printf("This is a scalar matrix");
            return 0;
        }
    }
    printf("This is not a scalar matrix");

    return 0;
}