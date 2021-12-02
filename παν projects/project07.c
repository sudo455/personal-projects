#include <stdio.h>

int main(){
    int x1,x2,x3,max;
    printf("give me the 1st number:");
    scanf("%d",&x1);
    printf("give me the 2st number:");
    scanf("%d",&x2);
    printf("give me the 3st number:");
    scanf("%d",&x3);
    max = x1 ;
    if(x2 > max){
        max = x2 ;
    }
    if(x3 > max){
        max = x3 ;
    }
    printf("the max nuber is %d\n",max);
    return 0;
}