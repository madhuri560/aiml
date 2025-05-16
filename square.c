#include<stdio.h>
int main(){
	int n,i;
	printf("enter the number of terms:");
	scanf("%d",n);
	for(i=1;i<=n;i++)
	{
		printf("square of %d=%d\n",i,i*1);
	}
	return 0;
}
