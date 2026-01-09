#include <stdio.h>
int main()
{double e=1.0;
double term=1.0;
int n=1;

while(term>=1e-6)
{
term=term/n;
e+=term;
n++;
}
printf("%.6f\n",e);
return 0;
}