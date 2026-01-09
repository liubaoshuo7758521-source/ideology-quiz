#include <stdio.h>
#include <string.h>

// 中心扩展函数：返回以left、right为中心的回文子串数量
int expandAroundCenter(char *s, int left, int right, int len) {
    int count = 0;
    while (left >= 0 && right < len && s[left] == s[right]) {
        count++;
        left--;
        right++;
    }
    return count;
}

int main() {
    char s[101];
    // 读取包含空格的字符串
    fgets(s, 101, stdin);
    int len = strlen(s);
    // 去掉fgets可能读取的换行符
    if (s[len-1] == '\n') {
        s[len-1] = '\0';
        len--;
    }

    int total = 0;
    for (int i = 0; i < len; i++) {
        // 奇数长度回文（中心是s[i]）
        total += expandAroundCenter(s, i, i, len);
        // 偶数长度回文（中心是s[i]和s[i+1]之间）
        total += expandAroundCenter(s, i, i+1, len);
    }

    printf("%d\n", total);
    return 0;
}