//输入 2k+1 个数，k 个数成对出现，1 个数唯一出现
#include <stdio.h>

int main() {
    int k;
    // 输入 k（题目隐含：总数字个数 = 2k+1）
    scanf("%d/n", &k);
    int total = 2 * k + 1;  // 总数字个数
    int result = 0;         // 异或结果初始化（0 异或任何数都不变）
    for (int i = 0; i < total; i++) {
        int num;
        scanf("%d", &num);
        result ^= num;  // 累计异或：成对数字抵消，最终保留唯一数
    }

    printf("%d\n", result);
    return 0;
}