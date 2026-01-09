#include <stdio.h>

int main() {
    char c;
    scanf("%c", &c);
    // 按行输出，控制空格和字符数
    printf("  %c\n", c);
    printf(" %c%c%c\n", c, c, c);
    printf("%c%c%c%c%c\n", c, c, c, c, c);
    printf(" %c%c%c\n", c, c, c);
    printf("  %c\n", c);
    return 0;
}