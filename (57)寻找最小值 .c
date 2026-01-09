#include <stdio.h>

int findMin(int arr[], int n) {
    if (n == 1) return arr[0];
    int rest_min = findMin(arr + 1, n - 1);
    return arr[0] < rest_min ? arr[0] : rest_min;
}

int main() {
    int n, arr[1000];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    printf("%d\n", findMin(arr, n));
    return 0;
}