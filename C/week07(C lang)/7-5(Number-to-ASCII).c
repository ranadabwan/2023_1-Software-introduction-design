
#include<stdio.h>


int main() {
	
    int i;
    long long num1 = 5215571311076468480L;
    //long long divider = 256L * 256 * 256 * 256 * 256 * 256;
    long long divider = 0x100000000000000;
    
    //printf("%lu", sizeof(long));
    
    for(i =  0; i < 8; i++)
    {
    	printf("%c", (char)(num1 / divider));
    	//divider = divider / 256;
    	divider /=256;
    
	}

    return 0;
}

