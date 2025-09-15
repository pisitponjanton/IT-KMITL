#include <stdio.h>
#include <string.h>

int main() {
    char str[101];
    scanf("%[^\n]", str);

    while (1) {
        char newstr[101];
        int idx = 0;
        int changed = 0;

        for (int i = 0; str[i] != '\0'; i++) {
            if (str[i] == str[i + 1]) {
                i++;
                changed = 1;
            } else {
                newstr[idx++] = str[i];
            }
        }
        newstr[idx] = '\0';

        if (changed) {
            printf("%s\n", newstr);
            strcpy(str, newstr);
        } else {
            break;
        }
    }

    return 0;
}
