#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>
void convert(int N,int R)
{char result[100];
 int i=0;
int isnegative=0;
 
 if(N<0)
 {isnegative=1;
  N=-N;
 }
 while(N!=0)
 {
     int remainder=N%R;
     if (remainder<10)
     {result[i]=remainder+'0';
     }
     else{
         result[i]=remainder-10+'A';
     }
     i++;
     N=N/R;
 }
if(isnegative)
{result[i]='-';
i++;
}
for (int j=i-1;j>=0;j--)
{printf("%c",result[j]);
}
printf("\n");
}
int main()
{
    int N,R;
    scanf("%d %d",&N,&R);
    if(N==0)
    {
        printf("0\n");
        return 0;
    }
    convert (N,R);
    return 0;
}