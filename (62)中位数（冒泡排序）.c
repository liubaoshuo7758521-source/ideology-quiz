#include <stdio.h>
#include <ctype.h>
int main() {
    int a,b,c,temp;
    scanf("%d%d%d",&a,&b,&c);//下面让三个数从小到大排序
    if(a>b){
        temp=a;//a的值存到仓库temp中避免丢失
        a=b;
        b=temp;

    }
    if(a>c){
        temp=a;
        a=c;
        c=temp;
    }
    if(b>c){
        temp=b;
        b=c;
        c=temp;
    }//只需比较b和c即可，因为a的位置已固定
    printf("%d",b);
    return 0;
}