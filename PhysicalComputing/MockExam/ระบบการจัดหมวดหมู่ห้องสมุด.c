#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char nums[6];
    scanf("%[^\n]", nums);
    int num = atoi(nums);

    if (num < 1000)
    {
        if (strlen(nums) == 2)
        {
            if (nums[1] == '0' || nums[1] == '5')
                printf("Science");
            else if (nums[1] == '3' || nums[1] == '7')
                printf("Literature");
            else
                printf("General Collection");
        }
        else if (strlen(nums) == 3)
        {
            if (nums[2] == '0' || nums[2] == '5')
                printf("Science");
            else if (nums[2] == '3' || nums[2] == '7')
                printf("Literature");
            else
                printf("General Collection");
        }
        else
        {
            if (nums[0] == '0' || nums[0] == '5')
                printf("Science");
            else if (nums[0] == '3' || nums[0] == '7')
                printf("Literature");
            else
                printf("General Collection");
        }
    }
    else
    {
        char tt[3];
        tt[0] = nums[2];
        tt[1] = nums[3];
        tt[2] = '\0';

        if (atoi(tt) % 4 == 0)
            printf("Reference");
        else if (atoi(tt) == 11 || atoi(tt) == 22 || atoi(tt) == 33)
            printf("History");
        else
            printf("Unclassified");
    }

    return 0;
}