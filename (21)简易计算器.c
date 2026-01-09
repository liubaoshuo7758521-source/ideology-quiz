#include <stdio.h>

int main() {
    float a, b, result;
    char op; // 运算符（+、-、*、/）

    // 第一步：输入两个数和运算符
    scanf("%f %c %f", &a, &op, &b);

    // 第二步：switch判断运算符，执行对应运算
    switch (op) {
        case '+':
            result = a + b;
            printf("%.2f %c %.2f = %.2f\n", a, op, b, result);
            break;
        case '-':
            result = a - b;
            printf("%.2f %c %.2f = %.2f\n", a, op, b, result);
            break;
        case '*':
            result = a * b;
            printf("%.2f %c %.2f = %.2f\n", a, op, b, result);
            break;
        case '/':
            // 处理除数为0的特殊情况
            if (b == 0) {
            } else {
                result = a / b;
                printf("%.2f %c %.2f = %.2f\n", a, op, b, result);
            }
            break;
        default:
            // 处理非法运算符
            break;
    }

    return 0;
}