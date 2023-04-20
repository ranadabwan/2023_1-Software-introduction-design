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

    scanf("%d %c %d", &num1, &op, &num2);

    switch (op) {
        case '&':
            result = num1 & num2;
            printb(result);
            break;

        case '|':
            result = num1 | num2;
            printb(result);
            break;

        case '+':
            result = num1 + num2;
            printb(result);
            break;

        default:
            printf("Invalid operator\n");
            return 1;
    }

    printf("  ");
    printb(num1);
    printf(" %c ", op);
    printb(num2);
    printf("\n");
    printf("--------------------------------\n");

    return 0;
}
	
	/*while(op != '&' && op != '|')
	{
		scanf("%d %c %d", &num1, &op, &num2);
	}
	if(op == '&')
	{
		result = num1 & num2;
	} else 
	
	{
		result = num1 | num2;
	}
	
	
	
	switch(op)
	{
	
		case'+':
			result = num1 & num2;
			//printb(result);
			break;
				
		case'|':
			result = num1 | num2;
			//printb(result);
			break;
			
		default:
			printf("Invalid operator\n");
			return 1;
				
		
	}


	
	printf("  ");
	printb(num1);
	printf(" %c ", op);
	printb(num2);
	printf("\n");
	printf("--------------------------------");
	//printf(" ");
	//printf("\n");
	printb(result);
	

	return 0;
}*/



