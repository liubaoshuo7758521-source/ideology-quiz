#include <stdio.h>

// 写法：固定3行4列
void func(int matrix[][4],int rows) {
    for (int i=0; i<rows; i++) { // 根据传入的rows参数处理相应行数
        for (int j=0; j<4; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }
}

int main() {
    int matrix1[3][4] = {{1,2,3,4}, {5,6,7,8}, {9,10,11,12}};
    func(matrix1,3); // 正常运行（3行4列）

    int matrix2[2][4] = {{13,14,15,16}, {17,18,19,20}};
    func(matrix2,2); // 正确传递行数参数，避免读取越界
    return 0;
}