#include <stdio.h>

int main(){
	
	int score;
	printf("Please input your score: ");
	scanf("%d", &score);
	
	
	if(score > 91 && score <= 100){
	printf("A");
	}
	if (score > 81 && score <= 90)
	{
	printf("B");
	}
	if (score > 71 && score <= 80)
	{
		printf("C");
	}
	if (score > 61 && score <= 70)
	{
		printf("D");
	}
	if(score >= 0 && score <= 60){
		printf("F");
	}
	return 0;
}
