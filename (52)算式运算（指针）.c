#include <stdio.h>
#include <stdlib.h>

int main() {
    char s[100];
    scanf("%s", s);  // 读取输入的算式
    
    char *op = s;
    // 寻找运算符
    while (*op != '+' && *op != '-' && *op != '*' && *op != '/' && *op != '\0') {
        op++;
    }
    if (!*op) {  // 没有找到合法运算符
        printf("illegal\n");
        return 0;
    }
    
    char operator = *op;  // 保存运算符
    *op = '\0';  // 分割字符串
    double a = atof(s);       // 左操作数
    double b = atof(op + 1);  // 右操作数
    
    // 处理除0错误
    if (operator == '/' && b == 0) {
        printf("illegal\n");
        return 0;
    }
    
    // 根据运算符计算并输出结果，保留两位小数
    switch (operator) {
        case '+': printf("%.2f\n", a + b); break;
        case '-': printf("%.2f\n", a - b); break;
        case '*': printf("%.2f\n", a * b); break;
        case '/': printf("%.2f\n", a / b); break;
    }
    
    return 0;
}

