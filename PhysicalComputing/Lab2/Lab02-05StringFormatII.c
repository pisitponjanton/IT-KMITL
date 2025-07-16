#include <stdio.h>

int main()
{
    float f_number = 3.1415;
    int number1 = 12345;
    int number2 = -6789;
    int number3 = 24500;
    printf("123456789012345678901234567890\n");
    printf("%d %d %d\n", number1, number2, number3);
    printf("%3d %3d %3d\n", number1, number2, number3);
    printf("%8d %8d %8d\n", number1, number2, number3);
    printf("%08d %08d %08d\n", number1, number2, number3);
    printf("%-8d %-8d %-8d\n", number1, number2, number3);
    printf("%10f\n", f_number);
    printf("%3f\n", f_number);
    printf("%-10f\n", f_number);
    printf("%-10.3f\n", f_number);
    printf("%10.2f\n", f_number);
    printf("%.1f\n", f_number);
    printf("%.3f\n", f_number);

    return 0;
}