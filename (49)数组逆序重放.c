#include <stdio.h>

int main() {
    int n;
    // 1. 输入数组长度
    scanf("%d", &n);
    
    int arr[10];
    for(int i = 0; i < n; i++) {
        // 2. 输入数组元素
        scanf("%d", &arr[i]);
    }
    
    // 3. 反向遍历输出（从最后一个元素到第一个）
    // 关键：最后一个元素的下标是 n-1，循环条件 i >= 0
    for (int i = n - 1; i >= 0; i--) {
        // 输出：最后一个元素无空格，其余元素后加空格（避免末尾多余空格）
        if (i == n - 1) {
            printf("%d", arr[i]);
        } else {
            printf(" %d", arr[i]);
        }
    }

    return 0;
}