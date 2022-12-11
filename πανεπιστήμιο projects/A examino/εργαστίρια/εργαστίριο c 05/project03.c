#include <stdio.h>
#include <stdlib.h>

int main(){
    int i,table[199],S,max,min;
    float MO;
    S=0;
    min=99;
    max=0;
    for(i=0;i<=199;i++){
        table[i] = rand() % 76;
        S += table[i];
        if(table[i] > max){
            max=table[i];
        }
        if(table[i] < min){
            min=table[i];
        }
        printf("table[%d]=%d\n",i,table[i]);
    }
    MO=S/199;
    printf("max=%d,min=%d,MO=%2.f\n",max,min,MO);
    return 0;
}