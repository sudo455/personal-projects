#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    srand(time(NULL));
    int i, j, score = 0, table[9];
    for(j = 0 ; j <= 100; j++){
        for(i = 0 ; i<= 9 ; i++){
            table[i] = rand() % 2;
        }
        for(int a = 0; a <= 3; a++){
            printf("table[%d] = %d\n", a, table[a]);
        }
        if((table[0] == 1 ) && (table[1] == 1) && (table[2] == 1) ){
            score+=1;
            printf("heads*3 at start \n");
        }else if ((table[0] != 1 ) && (table[1] != 1) && (table[2] != 1)){
            printf("tales*3 at start \n");

        }else{
            printf("somthing else\n");x
        }
    }
    printf("score of heads*3 at start is is: %d \n", score);
    return 0;
}