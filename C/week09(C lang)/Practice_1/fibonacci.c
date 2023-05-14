#include <stdio.h>

#define MAX_TABLE_SIZE 100000

int g_lut[MAX_TABLE_SIZE];

int g_lut[MAX_TABLE_SIZE];

void init_lut(void);
int fib(int n);
int fib_lut(int n);

int main(void) {
    int index = 45;
//    int result = fib(index);
    init_lut();
    int result = fib_lut(index); //change the function to the new one
	printf("Recursive fibonacci + lut method (%d) : %d\n", index, result);
}

void init_lut(void)
{
	
	int i;
	for(i = 0; i < MAX_TABLE_SIZE; ++i)
	{
		g_lut[i] = -1;
	}
	
	g_lut[0] = 0;
	g_lut[1] = 1;
}

int fib_lut(int n)
{
	if (g_lut[n] == -1)
	{
		
		g_lut[n] = fib_lut(n -1) + fib_lut(n -2);
		return g_lut[n];
	}
	else {
		return g_lut[n];
	}
}

int fib(int n) {
    if (n == 0) { 
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return fib(n-1) + fib(n-2);
    }
}
