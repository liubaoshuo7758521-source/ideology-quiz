#include <stdio.h>
#include <string.h>
struct stu{
  int id;
  char name[15];
  int grade;
  int cls;
  float score;  
};
int main(){
    int n;
    scanf("%d",&n);
    struct stu s[n],temp;
    for(int i=0;i<n;i++){
        scanf("%d %s %d %d %f",&s[i].id,s[i].name,&s[i].grade,&s[i].cls,&s[i].score);
    }
    for(int i=1;i<n;i++){
        for (int j=1;j<n-1-i;j++){
            if (s[j].score>s[j+1].score){
                temp=s[j];
                s[j]=s[j+1];
                s[j+1]=temp;
            }
            else if(s[j].score==s[j+1].score && strcmp(s[j].name,s[j+1].name)>0){
                temp=s[j];
                s[j]=s[j+1];
                s[j+1]=temp;
            }
            else if(s[j].score==s[j+1].score && strcmp(s[j].name,s[j+1].name)==0 && s[j].grade>s[j+1].grade){
                temp=s[j];
                s[j]=s[j+1];
                s[j+1]=temp;
            }
        }
    }
    for(int i=0;i<n;i++){
        printf("%d %s %d %d %.2f\n",s[i].id,s[i].name,s[i].grade,s[i].cls,s[i].score);
    }
    return 0;
}
