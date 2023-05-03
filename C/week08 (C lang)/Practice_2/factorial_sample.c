#include <stdio.h>
int fact(int n);

int main(void) {
    int index = 10;
    int result = fact(index);
    //int result = 1;
    printf("Factorial of %d is %d\n", index, result);
    return 0;
}

int fact(int n) {
    if (n < 0) {
        printf("Not defined negative factorial(far as I know...)\n");
        return -1;
    } else if(n == 0){
        return 1;
    } else {
    	return n * fact(n - 1);
	}
}
