#include <stdio.h>


int get_age(void)
{
	
	int age;	
    printf("How old are you?\n");
	scanf("%d", &age);
	return age ;
}


float get_elder(void)
{
	float user_number;
	printf("Did you know that lim x from 0 to infinite, (1 + x)^(1/x) is approximately?\n");
    scanf("%f", &user_number);
    return user_number;
}

char get_marrige_info(void)
{
	char answer;
	printf("Are you married?\n");
	scanf(" %c", &answer);
	return answer;
}

int main(void) {
    int age = -1;
    float e = -1;
    float e_real = 2.718281828459045235363027471352662;
    char is_married;   
	

	age = get_age();
	
    printf("Well you are %d years old, and you are ", age);
    if(age < 19)
	{
		printf("NOT");
    	
	}
    printf("allowed to drink\n");
    //printf("\n");
    printf("===============================\n");
    	printf("\n");

    e = get_elder();
    float delta = e - e_real;
    if(delta < 0)
    {
    	delta *= -1;
	}
	
	if (delta > 0.001)
	{
		printf("Not even close!\n");
	}
	else {
		printf("Well, it is fair enough!\n");
	}
	//printf("\n");
    printf("===============================\n");
    printf("\n");

	
	
	
    is_married = get_marrige_info();
    
    if(is_married == 'N')
    {
    	printf("How about dinner tonight?\n");
	} else if (is_married == 'Y')
	{
		printf("Oops sorry. Nevermind\n");
	}else {
		printf("What? I dont understand.\n");
	}
	
	printf("\n");
    printf("===============================\n");


    return 0;
}
