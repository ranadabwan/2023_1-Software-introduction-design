#include <stdio.h>

void upper(char * str);
void lower(char * str);
void string_copy(char * src, char * dst);
int string_len(char * str);
void concat(char * src_a, char * src_b, char * dst);
int parser(char * src, char * ret, char delimiter, int index);

void lower(char *str)

{
	
	int delta = 'a' - 'A';
	int i;
	for(i = 0; str[i] != '\0'; ++i)
	{
		if(str[i] >= 'A' && str[i] <= 'Z')
		{
			str[i] = str[i] + delta;
		}
	}
}

void upper(char * str)
{
	int delta = 'A' - 'a';
	int i;
	for(i = 0; str[i] != '\0'; ++i)
	{
		if(str[i] >= 'a' && str[i] <= 'z')
		{
			str[i] = str[i] +delta;
		}
	}
}


void string_copy(char * src, char * dst)
{
	int i = 0;
	for(; src[i] != '\0'; ++i)
	{
		dst[i] = src[i];
		
	}
	
	dst[i] = '\0';
}


int string_len(char * str)
{
	int cnt = 0;
	for (; str[cnt] != '\0'; ++cnt);
	return cnt;
}


void concat(char * src_a, char * src_b, char * dst)
{
	int str_a_len = string_len(src_a);
	string_copy(src_a, dst);
	string_copy(src_b, (dst + str_a_len));
}


int parser(char * src, char * ret, char delimiter, int index)
{
	int pos = 0;
	int cnt = 0;
	for(; src[pos] != '\0' && cnt < index; ++pos)
	{
		if(src[pos] == delimiter)
		{
			++cnt;
		}
	}
	if(src[pos] == '\0')
	{
		ret[0] = '\0';
		return -1;
	} else {
		int next_pos = pos;
		char backup_char;
		for(; src[next_pos] != '\0' && src[next_pos] != delimiter; ++next_pos);
		
		
		//Little trick
		backup_char = src[next_pos];
		src [next_pos] = '\0';
		string_copy(src + pos, ret);
		src[next_pos] = backup_char;
		
		return 1;
	}
}

int main(void) {
    char a = 'a';
    char z = 'z';
    char A = 'A';
    char Z = 'Z';
    char str_a[100];
    char str_b[100];
    char str_dst[200];
    int index = 3;

    printf("a : %d, z : %d, A : %d, Z : %d\n", (int) a, (int) z, (int) A, (int) Z);

    scanf("%s %s", str_a, str_b);
    printf("Original    : %s %s\n", str_a, str_b);
    
    upper(str_a);
    upper(str_b);
    printf("Upper           : %s %s\n", str_a, str_b);
    
    
    lower(str_a);
    lower(str_b);
    printf("Lower           : %s %s\n", str_a, str_b);
    
    
    //string_copy(str_a, str_b, str_dst);
    //printf("After Copy           :  %s %s\n",str_a, str_b);
    
    concat(str_a, str_b, str_dst);
    printf("After concat              : %s\n", str_dst);
    
    
    parser(str_a, str_dst, '|', 3);
    printf("Parser (%d) : %s\n", 3, str_dst);
    
    
  //Jun|Ho|Wohn|Nice|to|meet|you HAHAHA|123|456
return 0;
}
