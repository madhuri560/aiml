def fib(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
n=int(input("enter no of terms"))
c=fib(c)
print(c)



#include<stdio.h>
void printFib(int n) {
    if (n < 1) {
        printf("Invalid Number of terms\n");
