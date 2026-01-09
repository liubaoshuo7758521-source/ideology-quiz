
#include <stdio.h>
int main() {
    int num;
    // 读取非负整数
    scanf("%d", &num);
    // 以八进制格式输出（前面带0）
    printf("%#o\n", num);
    // 以十六进制大写格式输出（前面带0X）
    printf("%#X\n", num);
    return 0;
}