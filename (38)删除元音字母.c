#include <stdio.h>
#include <string.h>

int main() {
    char s[101];  // 定义字符数组存储输入（长度101，预留结束符位置）
    char result[101];  // 存储处理后的结果
    int i = 0, j = 0;  // i遍历原字符串，j记录结果字符串的下标

    // 输入字符串
    scanf("%s", s);

    // 遍历原字符串
    while (s[i] != '\0') {
        // 判断当前字符是否为元音字母
        if (!(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' ||
              s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U')) {
            result[j++] = s[i];  // 非元音则存入结果数组
        }
        i++;
    }
    result[j] = '\0';  // 给结果字符串加结束符

    // 输出处理后的字符串
    printf("%s\n", result);

    return 0;
}