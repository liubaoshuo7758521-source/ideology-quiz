#include<stdio.h>
#include<math.h>
int main() {
    int a = 12345;
    int b=1,c;
    int j;
    for(int i = 5; i > 0; i--) {
        b=1;  // 重置b的值
        j= (i+2)%5;
        while(j>0)
        {
            b *= 10;
            j--;
        }
        c = b/10;
        printf("%d", a/b%10);
    }
    return 0;
}