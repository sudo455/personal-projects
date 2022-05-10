#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){

    FILE *fp;
    int random_walker = 500;
    srand(time(NULL));
    fp = fopen("random_walker.csv","w+");

    for(int i = 0; i<= 1000; i++){

        if(rand() % 2 == 0 ){
            random_walker+=1;

        }else{
            random_walker-=1;
        }
        fprintf(fp, "%i,", random_walker);
    }
    
    printf("O perpatiths einai sto shmio %i \n", random_walker);
}