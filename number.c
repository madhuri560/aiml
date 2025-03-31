#include <stdio.h>

void printEvenNumbers(int start, int end)
{
    printf("Even numbers between %d and %d are: ", start, end);
    for (int i = start; i <= end; i++)
    {
        if (i % 2 == 0)
	{
            printf("%d ", i);

