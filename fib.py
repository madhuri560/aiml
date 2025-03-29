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
          return;
    }
    int prev1 = 1;
    int prev2 = 0;
      printf("%d ", prev2);
    if (n == 1)
        return;

    printf("%d ", prev1);
     for (int i = 3; i <= n; i++) {
        int curr = prev1 + prev2;
        prev2 = prev1;
        prev1 = curr;
        printf("%d ", curr);
    }
}
int main() {
    int n = 9;
    printFib(n);
    return 0;
}
