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


	unsigned int num1;

	printf("Enter the integer number you want its 2's Comp: ");
	scanf("%d", &num1);
	
	printb(num1);
	printb(~num1);
	printb(~(num1) + 1);
	printb(~num1);
	
	

	return 0;
}


