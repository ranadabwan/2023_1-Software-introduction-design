#include <stdio.h>

#define MAX_PRIME_NUM 200000 

int g_prime_list[MAX_PRIME_NUM];

int is_prime(int n);
void eratos(void);
void init_prime_list(void);


void init_prime_list(void)
{
	
	int i;
	
	for(i = 0; i < MAX_PRIME_NUM; ++i)
	{
		g_prime_list[i] = 1;
	}
}

int is_prime(int n)
{
	int i;
	for(i = 2; i < n; ++i)
	{
		if (n % i == 0)
		{
			return 0;
		}
	}
	
	return 1;
	}

void eratos(void)
{
	int i;
	for(i = 2; i < MAX_PRIME_NUM; ++i)
	{
		if (g_prime_list[i] == 0)
		{
			continue;
		}
		
		int i, j;
		for(i = 2; i * j < MAX_PRIME_NUM; ++j)
		{
			g_prime_list[i*j] = 0;
		}
	}
}


int main(void) {
	init_prime_list();
    // Do something clever
    // printf("Prime number list :");
    // int i;
    // for (i = 2; i < MAX_PRIME_NUM; ++i) {
	//	g_prime_list[i] = is_prime(i);
   // }

    
    eratos();
    
    printf("Prime number list :");
    int i;
    for(i = 2; i < MAX_PRIME_NUM; ++i)
    {
    	if (g_prime_list[i] == 1) 
    	{
    		printf("%d ", i);
		}
	/*}
        if (g_prime_list[i] == 1) {
            printf("%d ", i);
        }
    }*/
	}
    printf("\n");

}
