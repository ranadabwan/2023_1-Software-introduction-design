#include <stdio.h>
/*
int main(void) {
    int age = 17;
    float e = 2.71828182845904;
    char is_married = 'Y';
    printf("Hello I'm 17 years old\n");
    printf("Did you know that lim x from 0 to infinite, (1 + x)^(1/x) is approximately 2.7\n");
    printf("Guess what! My current state : marriage [N]\n");
    return 0;
}
*/


//edited version in lab class
int main(void) {
    int age = 17;
    float e = 2.71828182845904;
    char is_married = 'Y';
    printf("Hello I'm %d years old\n", age);
    printf("Did you know that lim x from 0 to infinite, (1 + x)^(1/x) is approximately %f\n", e);
    printf("Guess what! My current state : marriage [%c]\n", is_married);
    return 0;
}
