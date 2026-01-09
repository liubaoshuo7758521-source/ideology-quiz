#include <stdio.h>

#define MAX_SIZE 200 // 最终数组最大长度不超过200

int main() {
    int arr[MAX_SIZE];
    int n, k;

    // 读取初始数组长度
    scanf("%d", &n);
    // 读取初始数组元素
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    // 读取操作次数
    scanf("%d", &k);

    // 执行k次插入操作
    for (int i = 0; i < k; i++) {
        int index, num;
        scanf("%d %d", &index, &num);

        // 元素后移（从最后一个元素到插入位置）
        for (int j = n; j > index; j--) {
            arr[j] = arr[j - 1];
        }
        // 插入新元素
        arr[index] = num;
        n++; // 数组长度+1
    }

    // 输出最终数组
    for (int i = 0; i < n; i++) {
        if (i > 0) {
            printf(" "); // 元素间加空格
        }
        printf("%d", arr[i]);
    }
    printf("\n");

    return 0;
}
