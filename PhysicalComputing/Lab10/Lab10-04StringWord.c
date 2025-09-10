#include <stdio.h>
#include <string.h>

void to_lower_str(char s[]);
struct list 
{
    char name[150];
    int len;
};


int main()
{
    char text[150];
    scanf("%[^\n]", text);
    struct list words[50];
    int wordcount = 0;

    char str[50];
    int index = 0;
    for(int i = 0;; i++){
        if(text[i] == ' ' || text[i] == '\0'){
            if(index > 0){
                str[index] = '\0';
                strcpy(words[wordcount].name, str);
                words[wordcount].len = strlen(str);
                wordcount++;
                index = 0;
            }
            if(text[i] == '\0') break;
        }
        else{
            str[index] = text[i];
            index++;
        }
    }

    printf("%d words\n", wordcount);
    printf("----\n");

    for(int i = 0; i < wordcount; i++)
    {
        to_lower_str(words[i].name);
        printf("%s : %d\n", words[i].name, words[i].len);
    }

    return 0;
}

void to_lower_str(char s[]) {
    int i = 0;
    while (s[i] != '\0') {
        if (s[i] >= 'A' && s[i] <= 'Z')
            s[i] = s[i] - 'A' + 'a';
        i++;
    }
}