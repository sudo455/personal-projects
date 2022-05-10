#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){

    FILE *fp;
    int  random_walker, table_random_walker[1001]={0};
    srand(time(NULL));
    fp = fopen("random_walker100000.csv","w+");

    for(int j = 0; j <= 100000 ;j++){
        random_walker = 500;
        table_random_walker[random_walker]+=1;
        for(int i = 0; i <= 1000; i++){
            if(rand() % 2 == 0 ){
                random_walker+=1;
                table_random_walker[random_walker]+=1;

            }else{
                random_walker-=1;
                table_random_walker[random_walker]+=1;
            }
        }
    }

    fprintf(fp, "y, walker\n");
    for(int i = 0; i <= 1000; i++){fprintf(fp, "%d, %i\n", i,table_random_walker[i]);}
    
    printf("O perpatiths einai sto shmio %i \n", random_walker);
}