#include <stdio.h>

int main() {
    char c1, c2, c3, c4, c5;

    if (scanf(" %c %c %c %c %c", &c1, &c2, &c3, &c4, &c5) != 5) {
        return 1;
    }

    int d1 = c1 - '0';
    int d2 = c2 - '0';
    int d3 = c3 - '0';
    int d4 = c4 - '0';
    int d5 = c5 - '0';

    if (d1 < 1 || d1 > 9 ||
        d2 < 1 || d2 > 9 ||
        d3 < 1 || d3 > 9 ||
        d4 < 1 || d4 > 9 ||
        d5 < 1 || d5 > 9) {
        return 1;
    }

    putchar('0' + d3);
    putchar('0' + d4);
    putchar('0' + d5);
    putchar('0' + d1);
    putchar('0' + d2);

    return 0;
}
