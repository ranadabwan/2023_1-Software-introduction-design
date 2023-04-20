#include <stdio.h>

int main()
{
	int num, sum;
	
	printf("We will sum all numbers from 0 to N\n");
	printf("Please, input the number for N\n");
	scanf("%d", &num);
	
	sum = num * (num + 1) / 2;
	
	printf("Sum = %d", sum);
	
	return 0;
}
