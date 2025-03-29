#include<stdio.h>
int largestPower(int n, int p) {
  
    if (n == 0) 
        return 0;
    return n / p + largestPower(n / p, p);
}
int main() {
    int n = 10, p = 3;
