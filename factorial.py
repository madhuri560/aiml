n=5
fact=1
for i in range(1,n+1):
    fact*=i
    print(fact)


Factorial number
The factorial of a non-negative integer ( n ), denoted as ( n! ), is the product of all positive integers less than or equal to ( n ).

#include<stdio.h>
        {
            int factorial(int n)
{
    int res = 1, i;
    for (i = 2; i <= n; i++)
        res *= i;
    return res;

}
int main()
{
    int num = 5;
