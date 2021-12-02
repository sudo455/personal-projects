#include <stdio.h>

int main(){ //this will show the table of triliza
    int intex,i,j;
    intex = 0;
    for(i = 0; i <=2; i++){ 
        for(j = 0; j <=2; j++){
            intex = ((i+1)+(j+1))+intex;
            printf("i=%i j=%i intex=%i\n", i+1,j+1,intex);
        }
    }


    return 0;
}