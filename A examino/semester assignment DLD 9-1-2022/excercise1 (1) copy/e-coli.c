#include<stdio.h>
#include <stdbool.h>

int main(){
    int c=0, ma=0,mc=0,mg=0,mt=0,sum=0;
    char tga[] = "tga", ttggat[7] ;
    float pososto_a, pososto_c, pososto_g, pososto_t;
    bool flag = false;
    FILE *in ;
    in = fopen("ecoli1.dat","r");

    while(!feof(in)){

        switch(fgetc(in)){
            case 'a':
                ma++;
                break;
            case 'c':
               mc++;
               break;
            case 'g':
                mg++;
                break;
            case 't':
                mt++;
                break;
        }
        if(c>=800000 && c<=810000){
            if(){
                printf("H thesi apo c>=800000 && c<=810000 einai: %d \n", c);
            }
        }
        

        if(c>=2510000 && c<=2520000){
            if(fgets(tga, 4, in)){
                printf("H thesi apo c>=2510000 && c<=2520000 einai: %d \n", c);
            }
        }

        if(c>=800000 && c<=810000){
            if(fgets(ttggat, 7, in) == "ttggat"){
                sum++;
            }
        }


        c++;
    }
    pososto_a = (float) ma / (float) c * 100;
    pososto_c = (float) mc / (float) c * 100;
    pososto_g = (float) mg / (float) c * 100;
    pososto_t = (float) mc / (float) c * 100;
    printf("Emfanise pososta %f, %f, %f, %f %d \n",pososto_a, pososto_c, pososto_g, pososto_t, c);
    printf("To athroisma tou sumplegmatos ttfggat apo c>=800000 && c<=810000 einai: %d \n ",sum);

    return 0;
}