#include <stdio.h>

int main() {
    double a, b;      
    scanf("%lf %lf", &a, &b);
    // 计算商的整数部分
    int k = (int)(a / b);
    // 计算余数
    double remainder = a - k * b;
    // 保留6位小数输出
    printf("%.6f\n", remainder);
    return 0;
}