#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main (){
    
    double temp;
    
    srand(time(NULL));

    FILE *fp;

    for(int i = 10; i <= 1000000; i = i * 10){
        switch(i){
            case 10:
                fp = fopen("zero_to_one10.csv", "a+");
                break;
            case 100:
                fp = fopen("zero_to_one100.csv", "a+");
                break;
            case 1000:
                fp = fopen("zero_to_one1000.csv", "a+");
                break;
            case 10000:
                fp = fopen("zero_to_one10000.csv", "a+");
                break;
            case 100000:
                fp = fopen("zero_to_one100000.csv", "a+");
                break;
            case 1000000:
                fp = fopen("zero_to_one1000000.csv", "a+");
                break;
        }

        for(int j = 1; j <= i; j++){

            temp = (double) rand() / (double) RAND_MAX;
            fprintf(fp,"%lf\n", temp);

        }

    }

    fclose(fp);

    return 0;
}