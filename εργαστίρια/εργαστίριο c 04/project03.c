#include <stdio.h>
#define m29 29
#define m28 28
#define m30 30
#define m31 31

int main(){
    int x;
    do
    {
        printf("give me the number of the month:");
        scanf("%d",&x);
        if(x == 1){
            printf("ianouarios (%d hmeres) \n",m31);
        }
        else if(x == 2){
            printf("febrouarios (%d h %d hmeres) \n",m28,m29);
        }
        else if(x == 3){
            printf("martios (%d hmeres) \n",m31);
        }
        else if(x == 4){
            printf("aprilios (%d hmeres) \n",m30);
        }
        else if(x == 5){
            printf("maios (%d hmeres) \n",m31);
        }
        else if(x == 6 ){
            printf("iounios (%d hmeres) \n",m30);
        }
        else if(x == 7 ){
            printf("ioulios (%d hmeres) \n",m31);
        }
        else if(x == 8 ){
            printf("augoustos (%d hmeres) \n",m31);
        }
        else if(x == 9 ){
            printf("septemvrios (%d hmeres)\n",m30);
        }
        else if(x == 10 ){
            printf("octemvrios (%d hmeres) \n",m31);
        }
        else if(x == 11 ){
            printf("novemvrios (%d hmeres) \n",m30);
        }
        else if(x == 12 ){
            printf("dicemvrios (%d hmeres) \n",m31);
        }
        else{
            printf("o arithmos den antistixei se mhna \n");
        }
    } while (x>=13 || x<=0);
    return 0;
}