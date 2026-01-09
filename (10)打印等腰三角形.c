#include <stdio.h>
int main(void) 
{
    int n;
    scanf("%d", &n);
    int mid;
    mid = (n + 1) / 2;
    int k = 0;
    for (int i = 0; i < mid - 1; i++)// 上半部分的行数
     {
        for (int j = 0; j < n; j++) // 每行的列数
        {
            if (j == mid - k - 1 || j == mid + k - 1)// 打印上半部分的星号（只有边上才打印)
            {
                printf("*");
            }
            else if (j == n - 1) 
            {
                printf("\n");
            } 
            else 
            {
                printf(" ");
            }
        }
        k++;
    }
    for (int j= 0; j < n; j++) //打印最后一行
    {
        printf("*");
    }
    return 0;
}
