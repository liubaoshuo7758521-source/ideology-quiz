#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
void DTOB(int n){
    if(n>1)
        DTOB(n/2);
    printf("%d",n%2);// 递归调用，先处理高位
}
int main()
{int num;
scanf("%d",&num);
DTOB(num);
return 0;
}// 十进制转二进制，引入函数