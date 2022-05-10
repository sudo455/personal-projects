#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){

    FILE *fp;
    int random_walker = 500, table_random_walker[1000];
    srand(time(NULL));
    fp = fopen("random_walker.csv","w+");

    for (int i = 0; i <= 1000; i++){table_random_walker[i] = 0;}

    for(int i = 0; i<= 10000; i++){

        if(rand() % 2 == 0 ){
            random_walker+=1;
            table_random_walker[random_walker]+=1;

        }else{
            table_random_walker[random_walker]+=1;
            random_walker-=1;
        }
    }

    fprintf(fp, "y, walker\n");
    // for loop1
    for(int i = 0; i <= 1000; i++){

        fprintf(fp, "%d, %i\n", i,table_random_walker[i]);

    }
    
    printf("O perpatiths einai sto shmio %i \n", random_walker);
}