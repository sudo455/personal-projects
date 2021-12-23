#include <stdio.h>

int main(){
    int i;
    double triangularnumber;
    printf("loop|triangularnumber \n");
    for(i=5; i<=50; i=i+5){
        triangularnumber= i*(i+1)/2;
        printf("%d|%2.f\n",i, triangularnumber);
    }
    return 0;
}