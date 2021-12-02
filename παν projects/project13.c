#include <stdio.h>
int main(){
    int i,j,table[10][10];
    for(i=0;i<=10;i++){
        for(j=0;j<=10;j++){
            if(i == j){
                table[i][j]=1;
            }
            else if (i != j){
                table[i][j]=0;
            }
        }
    }
    return 0;
}