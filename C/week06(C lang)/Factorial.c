#include<stdio.h>

int main()
{
	printf("We will claculate N!\n");
	printf("Please, input the number for N\n");
	
	int i, num, Fact = 1;
	scanf("%d", &num);
	for (i = 1; i <= num; i++)
	{
		Fact = i * Fact;
	}
	printf("%d!: %d", num, Fact);
	
}
