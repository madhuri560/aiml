#include <stdio.h>

int main() {
    int day;
    printf("Enter a number (1-7) to get the corresponding weekday: ");
    scanf("%d", &day);
switch(day) {
        case 1:
            printf("Monday\n");
            break;
        case 2:
            printf("Tuesday\n");
            break;
	    case 3:
            printf("Wednesday\n");
            break;
        case 4:
            printf("Thursday\n");
            break;
