#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char *str;

    str = (char *) malloc(255 * sizeof(char));
    
    strcpy(str, "Porsche Arnold");
    
    char *ptr = str;
    while (*ptr != '\0')
        printf("%c", *ptr++);

    free(str);

    printf("\n");
    return 0;
}