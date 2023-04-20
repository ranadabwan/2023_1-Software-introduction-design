#include <stdio.h>

int main(){
	
	int a, b, quotient, remainder;
	
	printf("Please input teo numbers to get their remainder and quotient.\n");
	
	
	scanf("%d%d", &a, &b);
	
	
	quotient = a/b;
	remainder = a % b;
	
	printf("We divided %d by %d...\n", a, b);
	
	
	printf("Quotient: %d\n Remainder: %d", quotient, remainder);

	
	return 0;
}
