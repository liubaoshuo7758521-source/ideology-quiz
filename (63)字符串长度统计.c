#include <stdio.h>

// 自定义字符串长度统计函数（禁止用strlen）
int str_len(char str[]) {
    int len = 0;
    // 核心：遍历到字符串结束符'\0'为止
    while (str[len] != '\0') {
        len++; // 每遍历一个有效字符，长度+1
    }
    return len;
}

int main() {
    char str[100]; // 定义足够大的字符数组存储输入
    scanf("%s", str); // 输入字符串（不含空格）

    // 调用自定义函数计算长度
    int length = str_len(str);
    printf("%d\n", length);

    return 0;
}