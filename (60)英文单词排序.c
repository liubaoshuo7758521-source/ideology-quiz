#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 201

int is_upper_alpha(char *w) {
    for (int i=0; w[i]; i++)
        if (!isupper(w[i])) return 0;
    return 1;
}

void sort_words(char arr[][MAX], int n) {
    char tmp[MAX];
    for (int i=0; i<n-1; i++)
        for (int j=i+1; j<n; j++)
            if (strcmp(arr[i], arr[j])>0) {
                strcpy(tmp, arr[i]);
                strcpy(arr[i], arr[j]);
                strcpy(arr[j], tmp);
            }
}

int main() {
    int T;
    if (scanf("%d%*c", &T) != 1) {
        printf("输入错误\n");
        return 1;
    }
    
    for (int cas=0; cas<T; cas++) {
        char line[MAX], words[MAX][MAX];
        int wc=0, alpha_idx=0;
        char alpha_words[MAX][MAX];
        
        fgets(line, MAX, stdin);
        line[strcspn(line, "\n")] = '\0';
        char *tok = strtok(line, " ");
        while (tok) {
            strcpy(words[wc], tok);
            if (is_upper_alpha(tok))
                strcpy(alpha_words[alpha_idx++], tok);
            wc++, tok = strtok(NULL, " ");
        }
        
        sort_words(alpha_words, alpha_idx);
        
        printf("case #%d:\n", cas);
        int p=0;
        for (int i=0; i<wc; i++) {
            if (is_upper_alpha(words[i]))
                printf("%s", alpha_words[p++]);
            else
                printf("%s", words[i]);
            if (i != wc-1) printf(" ");
        }
        printf("\n");
    }
    return 0;
}