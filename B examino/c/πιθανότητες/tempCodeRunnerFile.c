#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    FILE *fp;
    int C1 = 0, C2 = 0, C3 = 0, C4 = 0, C5 = 0, C6 = 0;
    fp = fopen("dice_10.csv", "w+");
    for (int i = 0; i <= 10; i++){
        srand(time(NULL)+i);
        switch((rand()%6)+1){
            case 1:
                C1++;
            case 2:
                C2++;
            case 3:
                C3++;
            case 4:
                C4++;
            case 5:
                C5++;
            case 6:
                C6++;
        }
    }
    fprintf(fp," %d, %d, %d, %d, %d, %d", C1, C2, C3, C4, C5, C6);
    return 0;
}

