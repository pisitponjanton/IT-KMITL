#include "stdio.h"

int strange(int x, int y);

int main() {
    int a, b, c, d, r, s, t, u, v;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    r = strange(a, b);
    s = strange(r, c);
    t = strange(strange(s, b), strange(4, 2));
    u = strange(t+3, s+2);
    v = strange(strange(strange(u, a), b), c);
    printf("%d %d %d %d %d", r, s, t, u, v);
    return 0;
}

int strange(int x, int y) {
    int t, z;
    t = x + y;
    z = x * y;
    return t + z;
}
