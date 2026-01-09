#include <stdio.h>
#include <string.h>

int main() {
    int k;
    char s[1001]; // 字符长度不超过1000，留1位存结束符
    scanf("%d", &k);
    scanf("%s", s);//读入重复数和字符串
    
    int len = strlen(s);
    if (len == 0) { // 字符串为空的特殊情况
        printf("No\n");
        return 0;//输入验证
    }
    
    char current = s[0];
    int count = 1;
    for (int i = 1; i < len; i++)//开始循环
     {
        if (s[i] == current) //如果当前字符和前一个字符相同
        {
            count++;
            if (count >= k) {
                printf("%c\n", current);
                return 0;// 找到后直接返回
            }
        } else {
            current = s[i];
            count = 1;// 若不重复立刻结束，重置计数器
        }
    }
    
    // 最后检查一次（比如整个字符串是同一个字符的情况）
    if (count >= k) {
        printf("%c\n", current);
    } else {
        printf("No\n");//输出处理
    }
    return 0;
}