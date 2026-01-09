#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

// 函数声明
int hexToDecimal(const char *hex);
void decimalToBinary(int decimal);
void decimalToOctal(int decimal);
void decimalToHex(int decimal);
int isValidHex(const char *str);

int main() {
    int choice;
    char input[100];
    int decimal;

    printf("=== 数字进制转换器 ===\n");
    printf("1. 十六进制 -> 十进制、二进制、八进制\n");
    printf("2. 十进制 -> 二进制、八进制、十六进制\n");
    printf("3. 二进制 -> 十进制、八进制、十六进制\n");
    printf("0. 退出\n");

    while(1) {
        printf("\n请选择功能 (0-3): ");
        scanf("%d", &choice);

        if(choice == 0) {
            printf("程序结束。\n");
            break;
        }

        switch(choice) {
            case 1:
                printf("请输入十六进制数: ");
                scanf("%s", input);

                if(!isValidHex(input)) {
                    printf("错误：无效的十六进制数！\n");
                    break;
                }

                decimal = hexToDecimal(input);
                printf("十进制: %d\n", decimal);
                printf("二进制: ");
                decimalToBinary(decimal);
                printf("\n八进制: ");
                decimalToOctal(decimal);
                printf("\n十六进制: %X\n", decimal);
                break;

            case 2:
                printf("请输入十进制数: ");
                scanf("%d", &decimal);

                printf("二进制: ");
                decimalToBinary(decimal);
                printf("\n八进制: ");
                decimalToOctal(decimal);
                printf("\n十六进制: %X\n", decimal);
                printf("十进制: %d\n", decimal);
                break;

            case 3:
                printf("请输入二进制数: ");
                scanf("%s", input);

                // 验证二进制数
                int valid = 1;
                for(int i = 0; input[i]; i++) {
                    if(input[i] != '0' && input[i] != '1') {
                        valid = 0;
                        break;
                    }
                }

                if(!valid) {
                    printf("错误：无效的二进制数！\n");
                    break;
                }

                // 二进制转十进制
                decimal = 0;
                int len = strlen(input);
                for(int i = 0; i < len; i++) {
                    if(input[len - 1 - i] == '1') {
                        decimal += (int)pow(2, i);
                    }
                }

                printf("十进制: %d\n", decimal);
                printf("八进制: ");
                decimalToOctal(decimal);
                printf("\n十六进制: %X\n", decimal);
                printf("二进制: %s\n", input);
                break;

            default:
                printf("无效选择！请重新输入。\n");
                // 清空输入缓冲区
                while(getchar() != '\n');
        }
    }

    return 0;
}

// 十六进制转十进制
int hexToDecimal(const char *hex) {
    int decimal = 0;
    int len = strlen(hex);

    for(int i = 0; i < len; i++) {
        char c = toupper(hex[i]);
        int value;

        if(c >= '0' && c <= '9') {
            value = c - '0';
        } else if(c >= 'A' && c <= 'F') {
            value = 10 + (c - 'A');
        }

        decimal = decimal * 16 + value;
    }

    return decimal;
}

// 十进制转二进制
void decimalToBinary(int decimal) {
    if(decimal == 0) {
        printf("0");
        return;
    }

    int binary[32];
    int index = 0;

    while(decimal > 0) {
        binary[index++] = decimal % 2;
        decimal /= 2;
    }

    for(int i = index - 1; i >= 0; i--) {
        printf("%d", binary[i]);
    }
}

// 十进制转八进制
void decimalToOctal(int decimal) {
    if(decimal == 0) {
        printf("0");
        return;
    }

    int octal[32];
    int index = 0;

    while(decimal > 0) {
        octal[index++] = decimal % 8;
        decimal /= 8;
    }

    for(int i = index - 1; i >= 0; i--) {
        printf("%d", octal[i]);
    }
}

// 验证十六进制数
int isValidHex(const char *str) {
    if(strlen(str) == 0) return 0;

    for(int i = 0; str[i]; i++) {
        char c = toupper(str[i]);
        if(!((c >= '0' && c <= '9') || (c >= 'A' && c <= 'F'))) {
            return 0;
        }
    }
    return 1;
}