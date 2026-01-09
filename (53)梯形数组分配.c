#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    scanf("%d", &n);

    // 申请指针数组，用于存储每行的首地址
    int** arr = (int**)malloc(n * sizeof(int*));
    if (arr == NULL) {
        return 1;
    }

    int total_bytes = 0;
    // 累加指针数组占用的空间
    total_bytes += n * sizeof(int*);

    // 逐行为数组分配内存
    for (int i = 0; i < n; i++) {
        int row_len = i + 1;
        arr[i] = (int*)malloc(row_len * sizeof(int));
        if (arr[i] == NULL) {
            return 1;
        }
        // 累加当前行占用的空间
        total_bytes += row_len * sizeof(int);
    }

    // 输出总共使用的空间（字节数）
    printf("%d\n", total_bytes);

    // 先释放每行的内存
    for (int i = 0; i < n; i++) {
        free(arr[i]);
    }
    // 再释放指针数组的内存
    free(arr);

    return 0;
}