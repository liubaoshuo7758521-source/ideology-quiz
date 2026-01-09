#include <stdio.h>

int main() {
    int k;
    scanf("%d", &k);
    int n = 2 * k + 1; // 数组长度
    
    int candidate = 0; // 候选众数
    int count = 0;     // 候选数的计数
    
    // 边读边处理，无需存储整个数组（极致省空间）
    for (int i = 0; i < n; i++) {
        int num;
        scanf("%d", &num);
        
        if (count == 0) {
            candidate = num; // 计数为0，更新候选数
        }
        // 相同则计数+1，不同则计数-1（抵消）
        count += (num == candidate) ? 1 : -1;
    }
    
    printf("%d\n", candidate); // 最终候选数就是众数
    return 0;
}