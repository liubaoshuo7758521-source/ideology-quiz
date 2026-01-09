#include <stdio.h>

int main() {
    int n;
    printf("Please enter a positive integer: ");
    scanf("%d", &n);

    // 校验输入合法性：非正整数直接提示错误
    if (n <= 0) {
        printf("Input error\n");
        return 0; // 终止程序
    }

    // 特殊值处理：2是最小的素数
    if (n == 2) {
        printf("%d is a prime number\n", n);
        return 0;
    }

    // 素数判断核心标记：1代表是素数，0代表不是
    int is_prime = 1;
    // 优化循环：只需遍历到√n（减少循环次数，提升效率）
    for (int i = 2; i * i <= n; i++) {
        // 能被1和自身以外的数整除，说明不是素数
        if (n % i == 0) {
            is_prime = 0;
            break; // 找到因数后提前退出循环
        }
    }

    // 输出最终判断结果（1不是素数）
    if (is_prime && n != 1) {
        printf("%d is a prime number\n", n);
    } else {
        printf("%d is not a prime number\n", n);
    }

    return 0;
}