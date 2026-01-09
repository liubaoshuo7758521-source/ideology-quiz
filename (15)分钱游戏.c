#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);  // 输入总钱数
    
    // 最终三人钱数相等，必须能被3整除，否则直接无解
    if (n % 3 != 0) {
        printf("No Answer\n");
        return 0;
    }
    
    int target = n / 3;  // 最终每人的钱数
    int a3 = target, b3 = target, c3 = target;  // 第三次操作后的状态
    int a2, b2, c2;
    int a1, b1, c1;
    int a0, b0, c0;
    
    // 第一步：逆推第三次操作（丙分钱给甲、乙）
    // 甲、乙当前钱数必须是偶数，否则无法逆推
    if (a3 % 2 != 0 || b3 % 2 != 0) {
        printf("No Answer\n");
        return 0;
    }
    a2 = a3 / 2;
    b2 = b3 / 2;
    c2 = n - a2 - b2;
    
    // 第二步：逆推第二次操作（乙分钱给甲、丙）
    if (a2 % 2 != 0 || c2 % 2 != 0) {
        printf("No Answer\n");
        return 0;
    }
    a1 = a2 / 2;
    c1 = c2 / 2;
    b1 = n - a1 - c1;
    
    // 第三步：逆推第一次操作（甲分钱给乙、丙）
    if (b1 % 2 != 0 || c1 % 2 != 0) {
        printf("No Answer\n");
        return 0;
    }
    b0 = b1 / 2;
    c0 = c1 / 2;
    a0 = n - b0 - c0;
    
    // 验证初始钱数是否为正整数（不能为0或负数）
    if (a0 > 0 && b0 > 0 && c0 > 0) {
        printf("%d %d %d\n", a0, b0, c0);
    } else {
        printf("No Answer\n");
    }
    
    return 0;
}