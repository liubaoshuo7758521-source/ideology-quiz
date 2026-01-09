#include <stdio.h>
int countDigits(int num) {
    if (num == 0) return 1; // 0的位数是1
    int count = 0;
    num = num < 0 ? -num : num; // 处理负数
    while (num > 0) {
        num /= 10;
        count++;
    }
    return count;
}
int main() {
    int n;
    scanf("%d", &n);
    printf("count=%d\n", countDigits(n));
    return 0;
}