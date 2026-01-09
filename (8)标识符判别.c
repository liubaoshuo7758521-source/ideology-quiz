#include <stdio.h>
#include <ctype.h>  // 包含字符判断函数（isalpha、isalnum）的头文件

int main() {
    char s[100];  // 定义字符数组存储输入的标识符，假设长度不超过99
    int i, valid = 1;  // valid标记是否合法，初始为1（合法）

    // 读取用户输入的标识符
    scanf("%s", s);

    // 第一步：判断首字符是否合法（字母或下划线）
    if (!(isalpha(s[0]) || s[0] == '_')) {
        valid = 0;  // 首字符不合法，标记为0（不合法）
    } else {
        // 第二步：遍历后续字符，判断是否为字母、数字或下划线
        for (i = 1; s[i] != '\0'; i++) {  // '\0'是字符串结束符
            if (!(isalnum(s[i]) || s[i] == '_')) {
                valid = 0;  // 存在非法字符，标记为不合法
                break;      // 无需继续遍历，直接退出循环
            }
        }
    }

    // 根据标记输出结果
    if (valid) {
        printf("Yes\n");
    } else {
        printf("No\n");
    }

    return 0;
}