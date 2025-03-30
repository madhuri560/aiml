#include <stdio.h>

int reverseNum(int N) 
{
  
    int rev = 0;
    while (N > 0) {
        int dig = N % 10;
        rev = rev * 10 + dig;
        N /= 10;
    }
    return rev
