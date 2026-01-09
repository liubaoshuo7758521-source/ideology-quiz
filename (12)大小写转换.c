#include <stdio.h>
#include <ctype.h>
int main() {
    char ch;
    scanf("%c", &ch);
    if(islower(ch))
    {

         ch=toupper(ch);

         printf("%c\n", ch);

    }

    else if(isupper(ch))

    {

         ch=tolower(ch);

         printf("%c\n", ch);

    }

    return 0;
    

}