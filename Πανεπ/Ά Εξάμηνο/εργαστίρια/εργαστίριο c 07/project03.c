#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

struct point{
    double x, y, z;
};

double distance(struct point point1, struct point point2){
    return sqrt(pow(point1.x - point2.x, 2) + pow(point1.y - point2.y, 2)+ pow(point1.z - point2.z, 2));
}


struct point random_point(){
    struct point p;
    p.x= (double)rand() / (double)RAND_MAX;
    p.y= (double)rand() / (double)RAND_MAX;
    p.z= (double)rand() / (double)RAND_MAX;
    return p;
}


int main(){
    srand(time(0));
    int i,j, max_point_a, max_point_b;
    double max, distance_point_a_and_b;
    max = 0;
    max_point_a = 0;
    max_point_b = 0;
    struct point random_xyz_points[5]; //pou edw kaloume thn struct point rand_point() aplos vazoume se enan pinaka ta x, y, z (???????)
    printf("point(int)|   x   |   y   |   z \n");
    for(i=0; i < 5; i++){
        random_xyz_points[i] = random_point();
        printf("     %d    | %.3lf | %.3lf | %.3lf \n", i+1, random_xyz_points[i].x, random_xyz_points[i].y, random_xyz_points[i].z);
    }

    for(i=0; i < 5; i++){
        for(j=0; j < 5; j++){
            distance_point_a_and_b = distance(random_xyz_points[i], random_xyz_points[j]);
            if(distance_point_a_and_b > max){
                max = distance_point_a_and_b;
                max_point_a = i+1;
                max_point_b = j+1;
            }
        }
    }

    printf("the final maximum distance between point \n     %d    | %.3lf | %.3lf | %.3lf \n     %d    | %.3lf | %.3lf | %.3lf \nwith distance %.3lf\n", max_point_a, random_xyz_points[max_point_a].x, random_xyz_points[max_point_a].y, random_xyz_points[max_point_a].z, max_point_b, random_xyz_points[max_point_b].x, random_xyz_points[max_point_b].y, random_xyz_points[max_point_b].z, max);
// den kserw giati alla kamiafora emfanizei tersasteia noumera?????
    return 0;
}