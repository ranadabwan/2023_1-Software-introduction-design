#include <stdio.h>
#include <time.h>

int main() {
    char reg_num[14];
    int year, month, day, gender;
    time_t now = time(NULL);
    struct tm *current_time = localtime(&now);
    int current_year = current_time->tm_year + 1900;
    int current_month = current_time->tm_mon + 1;
    int current_day = current_time->tm_mday;
    int age;

    printf("Your reg. num: ABCDEF-GHIJKLM\n");
    scanf("%s", reg_num);

    // Extract year, month, and day from the first 6 digits
    year = 2000 + (reg_num[0] - '0') * 10 + (reg_num[1] - '0');
    month = (reg_num[2] - '0') * 10 + (reg_num[3] - '0');
    day = (reg_num[4] - '0') * 10 + (reg_num[5] - '0');

    // Calculate age
    age = current_year - year;
    if (current_month < month || (current_month == month && current_day < day)) {
        age--;
    }


	printf("Age: %d\n", age);
	
	
    // Determine gender
    gender = reg_num[7] - '0';
    if (gender % 2 == 0) {
        printf("Gender: Female\n");
    } else {
        printf("Gender: Male\n");
    }

    //printf("Age: %d\n", age);

    return 0;
}