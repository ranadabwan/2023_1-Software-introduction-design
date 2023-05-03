#include <stdio.h>

int fib(int n);

int main(void) {
    int index = 10;
    int result = fib(index);
    printf("%d th fibonacci number is %d\n", index, result);
}


/*int fib(int n){
	return 0;
}
*/


int fib(int n) {
    if (n == 0) { 
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return fib(n-1) + fib(n-2);
    }
}
