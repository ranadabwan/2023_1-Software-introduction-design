#include <stdio.h>
#include <string.h>

int main(){
	
	char c[100];
	int i = 0, upper;
	printf("Enter a string: ");
	gets(c);
	printf("\n");
	
	
	//its represntive will be the actual number + 32	
	//65 - 90
	
	
	while(c[i] != '\0')
	{
		
		if((c[i] >= 65) && (c[i] <= 90)) 
		{
		printf("%c\t", c[i]);
		c[i]= c[i] + 32; 
		printf("\n%c", c[i]);
		printf("\n%d", c[i]);
		printf("\n");
	}
	}
	else if((c[i] >= 97) && (c[i] <= 122))
	{
		printf("%c\t", c[i]);
		c[i]= c[i] - 32; 
		printf("\n%c", c[i]);
		printf("\n%d", c[i]);
		printf("\n");
	}
	i++;
	}
	
	
	
	return 0;
}

