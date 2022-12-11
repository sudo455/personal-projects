#include <stdio.h>

int main(){ //this will show the table of triliza
    int intex = 0 ,i,j;
    char aksdhg;
    bool lajdh;
    float f;
    double as;
    intex = 0;
    for(i = 0; i <=2; i++){ 
        for(j = 0; j <=2; j++){
            intex = ((i+1)+(j+1))+intex;
            printf("i=%i j=%i intex=%i\n", i+1,j+1,intex);
        }
    }


    return 0;
}