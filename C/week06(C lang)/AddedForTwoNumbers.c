#include <stdio.h>

int main( ){
	int a, b, neg;
	
	printf("Input two numbers: ");
	scanf("%d%d", &a, &b);
	
	neg = a + b;
	printf("%d + (%d) = %d", a, b, neg);
	
	return 0;
}
