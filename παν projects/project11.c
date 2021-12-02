#include <stdio.h>

int main(){
    int i,table[9];
    for(i=0;i <= 9 ; i++){
        table[i]=i+1;
        printf("Dwse enan arithmo:");
        scanf("%d",&table[i]);
        printf("\n");
    }
    printf("Table Number|Number\n");
    for(i=9;i>=0;i--){
        printf("%d|%d\n",i,table[i]);
    }
    return 0;
}