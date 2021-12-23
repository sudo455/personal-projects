#include <stdio.h>
#include <math.h>

struct point{
    double x, y, z;
};

int main(void){
    double d;

    struct point cords1;
    printf("give me the cords of the 1st point(x, y, z): ");
    scanf("%lf,%lf,%lf", &cords1.x, &cords1.y, &cords1.z);

    struct point cords2;
    printf("give me the cords of the 2nd point(x, y, z): ");
    scanf("%lf,%lf,%lf", &cords2.x, &cords2.y, &cords2.z);

    d=sqrt(pow(cords1.x - cords2.x, 2) + pow(cords1.y - cords2.y, 2) + pow(cords1.z - cords2.z, 2));

    printf("the final resault is %.3lf\n", d);

    return 0;
}
// compile with "gcc project02.c -lm -o project02.exe" because it have the function pow() and sqrt()
// if not compiled without -lm then it will output error message:
//      /usr/bin/ld: /tmp/cc34B2i5.o: in function `main':
//      project02.c:(.text+0xbe): undefined reference to `pow'
//      /usr/bin/ld: project02.c:(.text+0xf0): undefined reference to `pow'
//      /usr/bin/ld: project02.c:(.text+0x127): undefined reference to `pow'
//      /usr/bin/ld: project02.c:(.text+0x13b): undefined reference to `sqrt'
//      collect2: error: ld returned 1 exit status
