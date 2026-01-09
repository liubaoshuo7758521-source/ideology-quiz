#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            putchar(i == j ? '*' : '#');  // 对角线输出*，其余输出#
        }
        putchar('\n');
    }
    return 0;
}