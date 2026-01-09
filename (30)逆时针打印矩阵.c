#include <stdio.h>

// 顺时针遍历指定起始坐标和大小的方阵
// 参数说明：
// matrix: 原始矩阵
// result: 存储遍历结果的数组
// index: 结果数组的当前写入位置（指针形式，便于函数内修改）
// a: 方阵起始行坐标（左上角行）
// b: 方阵起始列坐标（左上角列）
// k: 方阵的边长
void t(char arr[51][51],char result[],int a,int b,int k,int *index){
    int top=a;
    int bottom=a+k-1;
    int left=b;
    int right=b+k-1;

    while(top<=bottom && left<=right){
        for(int i=left;i<=right;i++){
            result[(*index)++] = arr[top][i];
        }
            top++;

        for(int i=top;i<=bottom;i++){
            result[(*index)++] = arr[i][right];
        }
            right--;

        if(top<=bottom){
        for(int i=right;i>=left;i--){
            result[(*index)++] = arr[bottom][i];
        }
            bottom--;}

        if(left<=right){
        for(int i=bottom;i>=top;i--){
            result[(*index)++] = arr[i][left];
                }
        left++;}
    }}

    int main() {
    int n, index = 0;
    char arr[51][51] = {0}, result[2501] = {0};

    scanf("%d", &n);
    getchar();  
    // 吸收换行符

    for (int i = 0; i < n; i++) {
        scanf("%s", arr[i]);
    }   
    // 读取n行矩阵数据
    
    t(arr, result,  0, 0, n, &index);
    // 调用封装的函数：从坐标(0,0)开始，遍历大小为n的方阵

    // 输出结果
    printf("%s\n", result);

    return 0;
}