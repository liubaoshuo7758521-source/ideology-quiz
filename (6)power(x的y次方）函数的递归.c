#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float power (float x, int y)
{
    if (y == 0)
        return 1;
    else if (y < 0)
        return (1.0 / power(x, -y));
    else
        return x*power(x, y-1);
}

// 添加main函数作为程序入口
int main() {
    int x,y;
    scanf("%d %d", &x, &y);
    float res = power(x,y);
    printf("%.2f\n", res);  
    
    return 0;
}
