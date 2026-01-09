#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main() {
    int n, i;
    double sum = 0.0;

    printf("Enter a positive integer: ");
    scanf("%d", &n);

    for (i = 1; i <= n; ++i) {
        sum += 1.0 / i;
    }

    printf("Sum = %.2f\n", sum);
    return 0;
}