#include <stdio.h>
#include <ctype.h>
int main(){
    char ch;
    while((ch=getchar())!='\n'){
        if(isupper(ch)){
            putchar(tolower(ch));
        }
        else if(islower(ch)){
            putchar(toupper(ch));
        }
        else if(isdigit(ch))
        {   int num;
            num=(ch-'0'+3)%10;
            putchar(num+'0');

        }
        else if(ch==' '){
            putchar('\n');
        }
        else{
            putchar(ch);
        }
    }
}