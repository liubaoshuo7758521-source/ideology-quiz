#include <stdio.h>
struct stu{
    int id;
    char name[15];
    int grade;
    int cls;
    float score;
};

int main(){

    int n;
    struct stu arr[n];//循环外定义用于后续调用
    scanf("%d",&n);
    
for (int i=0;i<n;i++){
    scanf("%d %s %d %d",&arr[i].id,arr[i].name,&arr[i].grade,&arr[i].cls);
    };
    
for (int i=0;i<n;i++){
        int t_id;
        float t_score;//定义新变量
        scanf("%d %f",&t_id,&t_score);
        for (int j=0;j<n;j++){
            if (t_id==arr[j].id){
                arr[j].score=t_score;
            }//匹配绩点
        } }      
        
for (int i=0;i<n;i++){
           printf("%d %s %d %d %.1f\n",arr[i].id,arr[i].name,arr[i].grade,arr[i].cls,arr[i].score);
        }
        
    }
  

