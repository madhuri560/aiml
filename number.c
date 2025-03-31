#include <stdio.h>

void printEvenNumbers(int start, int end)
{
    printf("Even numbers between %d and %d are: ", start, end);
    for (int i = start; i <= end; i++)
    {
        if (i % 2 == 0)
	{
            printf("%d ", i);
   }
    }
    printf("\n");
}
void printOddNumbers(int start, int end)
{
    printf("Odd numbers between %d and %d are: ", start, end);
    for (int i = start; i <= end; i++) 
    {
	     if (i % 2 != 0) {
            printf("%d ", i);
        }
    }
    printf("\n");
}
int main() {
    int start, end;
    
    printf("Enter the start and end values: ");
    scanf("%d %d", &start, &end);
    
    printEvenNumbers(start, end);
    printOddNumbers(start, end);

    return 0;
}
