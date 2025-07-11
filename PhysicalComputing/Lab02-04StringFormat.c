#include <stdio.h>

int main()
{
    char text[13] = "Hello, world";
    printf("123456789012345678901234567890\n");
    printf("%s*\n", text);
    printf("%20s*\n", text);
    printf("%.20s*\n", text);
    printf("%-20s*\n", text);
    printf("%.10s*\n", text);
    printf("%-10s*\n", text);
    printf("%25.10s*\n", text);
    printf("%25.5s*\n", text);
    printf("%-25.10s*\n", text);
    return 0;
}