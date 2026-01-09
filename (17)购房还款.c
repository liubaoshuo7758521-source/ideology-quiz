#include <stdio.h>
#include <math.h>
int main()
{
    double d,p,r,m;
    scanf("%lf%lf%lf",&d,&p,&r);
    r=r/100.0;
     m=log(p/(p-r*d))/log(1+r);
    printf("%.0f\n",m);
    return 0;

}