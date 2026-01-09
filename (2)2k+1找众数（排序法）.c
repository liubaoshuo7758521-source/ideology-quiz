#include <stdio.h>
#include <stdlib.h>

// qsort排序的比较函数（升序）
int cmp(const void *a, const void *b) {
    return *(int*)a - *(int*)b;
}

int main() {
    int k;
    scanf("%d", &k);
    int n = 2 * k + 1;
    int nums[n]; // 存储数组（题目允许，不算额外容器）
    
    // 读取输入
    for (int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }
    
    // 排序（C标准库qsort，仅用栈空间，无额外容器）
    qsort(nums, n, sizeof(int), cmp);
    
    // 排序后，中间元素一定是众数（众数占比超过一半）
    printf("%d\n", nums[k]); // 中间索引是k（0-based）
    
    return 0;
}