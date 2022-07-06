#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){

    FILE *fp;
    int random_walker_X = 500, random_walker_Y = 500;
    srand(time(NULL));
    fp = fopen("random_walker_2D.csv","w+");

    for(int i = 0; i<= 1000; i++){

        if(rand() % 2 == 0 ){
            random_walker_X+=1;

        }else{
            random_walker_X-=1;
        }

        if(rand() % 2 == 0 ){
            random_walker_Y+=1;

        }else{
            random_walker_Y-=1;
        }

        fprintf(fp, "%i, %d\n", random_walker_X, random_walker_Y);
    }
    
    printf("O perpatiths einai sto shmio X=%i, Y=%d \n", random_walker_X,random_walker_Y);
}