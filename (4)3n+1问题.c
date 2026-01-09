#include <stdio.h>  // 包含标准输入输出库，用于printf和scanf函数

// 计算单个数字n的循环长度（3n+1问题）
int cycleLength(int n) {
    int length = 1;  // 初始化长度为1，因为即使n=1也算一步
    while (n != 1) {  // 当n不等于1时继续循环
        if (n % 2 == 1) {  // 判断n是否为奇数（取余数为1）
            n = 3 * n + 1;  // 如果是奇数，执行3n+1操作
        } else {  // 如果n是偶数
            n = n / 2;  // 执行n/2操作
        }
        length++;  // 每执行一次操作，长度加1
    }
    return length;  // 返回计算得到的循环长度
}

int main() {  // 主函数，程序入口
    int i, j;  // 声明两个整型变量，用于存储输入的范围
    while (scanf("%d %d", &i, &j) == 2) {  // 循环读取输入，直到输入结束（scanf返回值为2表示成功读取两个整数）
        int start = i, end = j;  // 创建start和end变量保存输入值
        // 确保start <= end，保证循环范围正确
        if (start > end) {  // 如果start大于end，需要交换
            int temp = start;  // 使用临时变量保存start的值
            start = end;  // 将end的值赋给start
            end = temp;  // 将临时变量（原start的值）赋给end
        }
        
        int maxLen = 0;  // 初始化最大长度为0
        // 计算范围内所有数的循环长度，找出最大值
        for (int num = start; num <= end; num++) {  // 遍历从start到end的所有整数
            int len = cycleLength(num);  // 计算当前数字的循环长度
            if (len > maxLen) {  // 如果当前长度大于已知最大长度
                maxLen = len;  // 更新最大长度
            }
        }
        
        printf("%d %d %d\n", i, j, maxLen);  // 按原顺序输出i、j和最大循环长度
    }
    return 0;  // 程序正常结束，返回0
}