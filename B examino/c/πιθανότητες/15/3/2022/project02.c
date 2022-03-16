#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int main (){
    
    double temp, x, y;
    
    srand(time(NULL));

    FILE *fp;

    fp = fopen("project2_10000.csv", "a+");
    fprintf(fp, "-log(1-xi), xi^2, (xi^j)^2 + (xi^k)^2, (xi^j)^2 + (xi^k)^2 + (xi^m)^2 + (xi^n)^2 + (xi^l)^2");
    for(int j = 1; j <= 10000; j++){
        x = (double) rand() / (double) RAND_MAX;
        y = (-1) * log(1-x);
        fprintf(fp, "%lf,", y);
        y = pow(x, (double)2);
        fprintf(fp, "%lf,", y);
        y = pow(pow(x, rand()), 2.0) + pow(pow(x, rand()), 2.0);
        fprintf(fp, "%lf,", y);
        y = pow(pow(x, rand()), 2.0) + pow(pow(x, rand()), 2.0) + pow(pow(x, rand()), 2.0) + pow(pow(x, rand()), 2.0) + pow(pow(x, rand()), 2.0);
        fprintf(fp, "%lf\n", y);

    }

    fclose(fp);

    return 0;
}