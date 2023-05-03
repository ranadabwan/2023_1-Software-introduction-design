#include <stdio.h>

void rumor(int friends, int cnt);

int main(void) {
    rumor(4,0);
    return 0;
}

void rumor(int friends, int cnt) {
	if (friends == cnt) {
		//Reached!
		int i;
		for(i = 0; i < cnt; ++i)
		{
			printf(" ");
		}
		printf("UFO IS COMMING!\n");
	} else {
		int i;
		for(i = 0; i < cnt; ++i) {
			
			printf(" ");
		}
		printf("Big news! Friend of mine told me that....\n");
		//keep searching for the first friend
    	rumor(friends, cnt + 1);
    	
    	
		for(i = 0; i < cnt; ++i) {
			
			printf(" ");
		}
		printf("This is insane! Isn't it?\n");

	}
    
}
