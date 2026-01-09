# include <stdio.h>
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}
int main() {
    int x=5,y=10;
    scanf("%d %d",&x,&y);
    printf("before swap:x=%d y=%d\n",x,y); // 修正格式字符串中的缺失等号
    swap(&x,&y);
    printf("after swap:x=%d y=%d\n",x,y);  
    return 0;
}
