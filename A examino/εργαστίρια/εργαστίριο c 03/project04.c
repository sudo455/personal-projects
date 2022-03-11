#include <stdio.h>

int main(){
    int k=4;
    int i, j;
    i=1;
    while(i <= k){
        j=1;
        while(j <= k){
            printf("i=%i|j=%i \n", i, j);
            j+=1;
        }
        i+=1;
    }
    return 0;
}