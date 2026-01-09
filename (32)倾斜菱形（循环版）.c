#include <stdio.h>

int main() {
    // 上半部分：4行，星号数量递增
    for (int i = 0; i < 4; i++) {
        // 输出空格（每行空格数递减）
        for (int j = 0; j < 3 - i; j++) {
            printf(" ");
        }
        // 输出星号（每行星号数为2*i+1，递增）
        for (int k = 0; k < 2 * i + 1; k++) {
            printf("*");
        }
        // 换行
        printf("\n");
    }
    
    // 下半部分：3行，星号数量递减
    for (int i = 0; i < 3; i++) {
        // 输出空格（每行空格数递增）
        for (int j = 0; j < i +1; j++) {  // 原代码中j < i;可能为笔误，修正为j < i+1以匹配输出
            printf(" ");
        }
        // 输出星号（每行星号数为5-2*i，递减）
        for (int k = 0; k < 5 - 2 * i; k++) {
            printf("*");
        }
        // 换行
        printf("\n");
    }
    
    return 0;
}