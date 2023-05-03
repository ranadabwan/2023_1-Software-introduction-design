#include <stdio.h>

void budweiser(int size, int depth);

int main(void) {
    budweiser(4, 0);
    return 0;
}

void print_star(int size, int depth)
{
	int i;
	
	for (i = 0; i < depth; ++i)
	{
		printf("*");
	}
	
	
	for (i = 0; i < 2 * size +  1 - depth - depth; ++i)
		{
			printf(" ");
		}
		
		
		for (i = 0; i < depth; ++i)
	{
		printf("*");
	}
	
	printf("\n");
}

void budweiser(int size, int depth) {

	int i;
	
    if (depth == size) {
    	
    	for(i = 0; i < 2 * size + 1; ++i)
    	{
    		printf("*");
		}
    	
    	printf("\n");
    } else {
		depth += 1;    	
    	print_star(size, depth);
    	
    	budweiser(size, depth);
    	
    	
    	print_star(size, depth);
    
    	
	}
}

