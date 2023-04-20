#include <stdio.h>

void printb(int number) {
	for (int i = 0; i < 32; i++) {
		if ((i % 8) == 0) {
			printf(" ");
		}
		printf("%d", !!(number & 0x8000000000000000UL));
		number <<= 1;
	}
	printf("\n");
	fflush(stdout);
}

int main(void) {

	//int num = 245;
	//printb(num);
	printf("Enter the integer number you want to convert to binary: ")
	scanf("%d", &num);
	printf
	printb("\nThe converted number is: ", num);
	return 0;
}
