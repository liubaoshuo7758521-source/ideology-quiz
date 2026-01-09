#include <stdio.h>

int main(){
    int n,temp;
    scanf("%d", &n);
    int arr[100];
    for(int i=0;i<n;i++){//下标值到n-1
        scanf("%d", &arr[i]);}
        for (int i=0;i<n-1;i++){//排序时不取n-1
            for (int j=0;j<n-i-1;j++){
        if(arr[j]>arr[j+1]){
            temp=arr[j];
            arr[j]=arr[j+1];
            arr[j+1]=temp;
        }}}
       
    for (int i=0;i<n;i++){
        if (i==0){
            printf("%d", arr[i]); }
        else {
        printf(",%d", arr[i]);
    }}
    printf("\n");
    return 0;
    
}