#include <stdio.h>

int main(){
    int i;
    do
    {
        printf("give me the number of the month:");
        scanf("%d",&i);
        if(i == 1){
            printf("ianouarios \n");
        }
        else if(i == 2){
            printf("febrouarios \n");
        }
        else if(i == 3){
            printf("martios \n");
        }
        else if(i == 4){
            printf("aprilios \n");
        }
        else if(i == 5){
            printf("maios \n");
        }
        else if(i == 6 ){
            printf("iounios \n");
        }
        else if(i == 7 ){
            printf("ioulios \n");
        }
        else if(i == 8 ){
            printf("augoustos \n");
        }
        else if(i == 9 ){
            printf("septemvrios \n");
        }
        else if(i == 10 ){
            printf("octemvrios \n");
        }
        else if(i == 11 ){
            printf("novemvrios \n");
        }
        else if(i == 12 ){
            printf("dicemvrios \n");
        }
        else{
            printf("o arithmos den antistixei se mhna \n");
        }
    }
    while(i>=13 || i<=0);
    return 0;
}