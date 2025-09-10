#include <stdio.h>
#include <string.h>

void delete_chars(char str[], int c1, int c2) {
    int len = strlen(str);
    char newstr[len];
    int index = 0;

    for (int i = 0; i < len; i++) {
        if (i != c1 && i != c2) {
            newstr[index++] = str[i];
        }
    }
    newstr[index] = '\0';

    strcpy(str, newstr);
}

int main() {
    char str[100];
    scanf("%[^\n]", str);

    while (1) {
        int changed = 0;

        for (int i = 1; str[i] != '\0'; i++) {
            if (str[i] == str[i - 1]) {
                delete_chars(str, i, i - 1);
                printf("%s\n", str);
                changed = 1;
                break;
            }
        }

        if (!changed) break;
    }


    return 0;
}
