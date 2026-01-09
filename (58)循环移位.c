#include <stdio.h>
#include <math.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);  // 直接读取两个整数（n为原数字，m为移位次数）
    
    // 步骤1：计算n的位数digit_count
    int temp = n, digit_count = 0;
    do {
        digit_count++;
        temp /= 10;
    } while (temp != 0);
    
    // 步骤2：处理移位次数（取模，避免无效移位）
    m = m % digit_count;
    if (m == 0) {  // 移位0次，直接输出原数
        printf("%d %d\n", digit_count, n);
        return 0;
    }
    
    // 步骤3：计算分割位置，分离后m位和前(digit_count - m)位
    int power = pow(10, m);  // 10^m，用于分割数字
    int last_m = n % power;  // 最后m位数字
    int first_part = n / power;  // 前面(digit_count - m)位数字
    
    // 步骤4：组合得到循环右移后的结果
    int result = last_m * pow(10, digit_count - m) + first_part;
    
    // 输出结果（位数 + 空格 + 移位后数字）
    printf("%d %d\n", digit_count, result);
    return 0;
}