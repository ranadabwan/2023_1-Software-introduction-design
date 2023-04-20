#include <stdio.h>

void printb(int val) {
	
	int i;
	for (i = 0; i < 32; i++) {
		if ((i % 8) == 0) {
			printf(" ");
		}
		printf("%d", !!(val & 0x8000000000000000UL));

		val <<= 1;

	}
	printf("\n");
	fflush(stdout);
}


int main(void) {


	int num1, num2, result;
	char op;
	printf("Enter two integer number you want add them in thier binary forms: ");
	scanf("%d %c %d", &num1, &op, &num2);
	
	
	switch(op)
	{
		default:
		case '+':
			result = num1 + num2;
			//printf("\nThe addition of the two binary numbers: %d",result);
			break;
			
			
		case '-':
			result = num1 - num2;
			//printf("\nThe addition of the two binary numbers: %d", result);
			break;
			
			
	}
	
	printf("  ");
	printb(num1);
	printf(" %c ", op);
	printb(num2);
	printf("\n");
	printf("--------------------------------");
	printf(" ");
	printf("\n");
	printb(result);
	

	return 0;
}

