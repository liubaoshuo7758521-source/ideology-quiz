#include <stdio.h>

int main() {
    int n;
    // 读取数组长度
    scanf("%d", &n);
    
    int arr[100]; // 数组最大长度100
    // 读取数组元素
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    // 计数数组：count[0]对应-50，count[100]对应50
    int count[101] = {0};
    for (int i = 0; i < n; i++) {
        // 将元素映射到0~100的下标
        count[arr[i] + 50]++;
    }
    
    // 按元素大小（-50到50）输出
    for (int i = 0; i <= 100; i++) {
        if (count[i] > 0) {
            // 下标转换为原元素值
            printf("%d %d\n", i - 50, count[i]);
        }
    }
    
    return 0;
}