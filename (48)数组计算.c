#include <stdio.h>

int main() {
    // 1. 定义包含 100 个 double 元素的数组
    double data[100];
    
    // 2. 填充数组
    for (int i = 0; i < 100; i++) {
        int num = 2 * (i + 1); // 第 i 项对应的起始数：2、4、6…200
        data[i] = 1.0 / (num * (num + 1) * (num + 2));
    }
    
    // 3. 计算交替和：data[0]-data[1]+data[2]-…-data[99]
    double sum = 0.0;
    for (int i = 0; i < 100; i++) {
        if (i % 2 == 0) {
            sum += data[i]; // 偶数索引（0、2…）加
        } else {
            sum -= data[i]; // 奇数索引（1、3…）减
        }
    }
    
    // 4. 计算最终结果并输出
    double result = sum * 4.0 + 3.0;
    printf("%.4f\n", result);
    
    return 0;
}