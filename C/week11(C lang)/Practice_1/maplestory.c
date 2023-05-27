#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>

#define MAX_MONSTER_NUM 10
#define MAX_NAME_SIZE 30

int TICK = 0;
int MONSTER_GEN = 3;


// atk : attack point
// name : name of user
struct _character {
	
	int atk;
	char name[MAX_NAME_SIZE];
};
typedef struct _character Character;

// atk : attack point
// is_exist : 0 to dead, 1 to alive
struct _monster {
	
	int atk;
	int is_exist;
};
typedef struct _monster Monster;

// Show the status of given character
void character_show_stat(const Character * character);
// Initialize given character
void character_init(Character * character);

// Show the status of given monster
void monster_show_stat(const Monster * monster);
// Initialize given monster
void monster_init(Monster * monster);
// Generate new monster (if there is space in monsters)
void monster_generate(Monster * monsters);

// Choose 0 : Use Item, 1 : Fight, 2 : Do nothing
void combat(Character * character, Monster * monsters);


void character_init(Character * character)
{
	character->atk = 0;
	printf("Please input your nickname\n");
	scanf("%s", character->name);
	char yesno = 'n';
	
	while(1)
	{
		character->atk = (rand()%10) + 1;
		character_show_stat(character);
		printf("Are you satisfied? (Y/N) \n");
		scanf(" %c", &yesno);
		
		if(yesno == 'Y' || yesno == 'y')
		{
			break;
		}
	}
}

void monster_init(Monster * monster)
{
	int atk;
	atk = (rand() %5 + TICK) + 1;
	monster->atk = atk;
}


void character_show_stat(const Character * character)
{
	printf("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n");
	printf("USER NAME               : %s\n", character->name);
	printf("USER ATTACK POINT : %d\n", character->atk);
	printf("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n");
}


void monster_show_stat(const Monster * monster)
{
	printf("ATTACK POINT  : %d\n", monster->atk);
}

void monster_generate(Monster * monsters)
{
	
	int i;
	
	for(i = 0; i < MAX_MONSTER_NUM; ++i)
	{
		if(monsters[i]. is_exist == 0)
		{
			monster_init(&monsters[i]);
			monsters[i].is_exist = 1;
			return ;
		}
	}
}


int main(void) {

    srand(time(NULL));
    Character user;
     Monster monsters[MAX_MONSTER_NUM];
     int i;
     
     
     for ( i = 0; i < MAX_MONSTER_NUM; ++i) {
         monsters[i].is_exist = 0;
     }

    printf("***********************************\n");
    printf("Welcome to Maple Story\n");
    printf("***********************************\n");

    character_init(&user);
    character_show_stat(&user);


     while (user.atk > 0) {
         printf("+++++++++++++++++++++++++++++++++++\n");

         if (TICK % MONSTER_GEN == 0) {
         	monster_generate(monsters);

         }
         
         int i;
         
         
         for ( i = 0; i < MAX_MONSTER_NUM; ++i)
         {
         	if(monsters[i].is_exist == 1)
         	{
         		printf("^^^^^^^^^^^^^^^^^^^^^^^^^^\n");
         		monster_show_stat(&monsters[i]);
         		printf("^^^^^^^^^^^^^^^^^^^^^^^^^^\n");

         		
			 }
		 }
         char yesno = 'n';
         printf("Keep generating momsters?\n");
         scanf(" %c", &yesno);
         if (yesno == 'n' || yesno == 'N')
         {
         	break;
		 }

        // character_show_stat(&user);

        // combat(&user, monsters);

         printf("===================================\n");
         printf("\n\n\n\n");
         TICK++;
     }
    return 0;
}

/*
void monster_show_stat(const Monster * monster) {
    printf("ATTACK POINT  : %d\n", monster->atk);
    printf("HEALTH POINT  : %d\n", monster->hp);
}
*/

/*
void character_show_stat(const Character * character) {
    printf("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n");
    printf("USER NAME          : %s\n", character->name);
    printf("USER ATTACK POINT  : %d\n", character->atk);
    printf("USER HEALTH POINT  : %d\n", character->hp);
    printf("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n");
}
*/
