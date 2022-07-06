#include <stdio.h>

/*global struct*/
struct time {
    int hours, minutes, seconds;
};

void test_main_1(int h1, int m1, int s1, int h2, int m2, int s2){
    struct time result;
    result.hours = h1 + h2;
    result.minutes = m1 + m2;
    result.seconds = s1 + s2;
    printf("the resault is hours:%d minutes:%d seconds:%d \n", result.hours, result.minutes, result.seconds);
}

int main(void){
    struct time time1;
    printf("give me the data of the 1st period(h, m, s):");
    scanf("%d %d %d", &time1.hours, &time1.minutes, &time1.seconds);
    struct time time2;
    printf("give me the data of the 2st period(h, m, s):");
    scanf("%d %d %d", &time2.hours, &time2.minutes, &time2.seconds);
    test_main_1(time1.hours, time1.minutes, time1.seconds, time2.hours, time2.minutes, time2.seconds);
    return 0;
}