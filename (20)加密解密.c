/*编写一个 C 语言程序，实现以下功能：
从控制台读取单个字符；
首先将该字符（如果是大写字母）转换为小写字母；
对转换后的字符进行判断和处理：
若为元音字母（a、e、i、o、u）：直接输出该字符；
若为其他小写字母（非元音）：将该字母在字母表中向后偏移 3 位（如 b→e、y→b、z→c），输出偏移后的字母；
若不是字母（如数字、符号、空格等）：输出 error；
程序仅处理单个字符输入，无需考虑多字符场景。*/
#include <stdio.h>
#include <ctype.h>
int main(){
    char ch=getchar();
    if(isupper(ch))
    {
ch=tolower(ch);//大写转小写
    }
   if(ch=='a'||ch=='e'||ch=='i'||ch=='o'||ch=='u')
{
    printf("%c\n",ch);
}//元音字母不变
    else if(isalpha(ch))
{
    printf("%c\n",(ch-'a'+3)%26+'a');//重点，先算偏移量+3，再对26取模，最后转回字符
}//其他字母加3
else
{
    printf("error\n");
}//非字母输出error

    return 0;
}