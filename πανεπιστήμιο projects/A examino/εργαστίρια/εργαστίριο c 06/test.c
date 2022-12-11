#include <stdio.h>

int main(){
    int x1, y1;
    double x, y, rs, rs2;
    x=12;
    x1=12;
    y=5;
    y1=5;
    rs=x/y;
    rs2=x1/y1;
    printf("the result is:%.3lf\n", rs);
    printf("the result is:%.3f\n", rs2);
}