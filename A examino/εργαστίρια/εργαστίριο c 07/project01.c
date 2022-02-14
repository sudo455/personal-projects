#include <stdio.h>

struct time {
    int hours, minutes, seconds;
};

int main(){
    struct time time1;
    printf("give me the data of the 1st period(h, m, s):");
    scanf("%d,%d,%d", &time1.hours, &time1.minutes, &time1.seconds);
    struct time time2;
    printf("give me the data of the 2st period(h, m, s):");
    scanf("%d,%d,%d", &time2.hours, &time2.minutes, &time2.seconds);
    struct time rs;
    rs.hours = time1.hours+time2.hours;
    rs.minutes = time1.minutes+time2.minutes;
    rs.seconds = time1.seconds+time2.seconds;
    printf("the final resault is: %d %d %d\n", rs.hours, rs.minutes, rs.seconds);
    return 0;
}