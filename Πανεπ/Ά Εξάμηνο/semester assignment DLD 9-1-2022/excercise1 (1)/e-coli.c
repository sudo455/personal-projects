#include <stdio.h>

int main(void) {
    int m_a=0, m_c=0, m_g=0, m_t=0, m_ttggat=0, c=0, i, triplet, ft;
    char find[6];
    double e_a, e_c, e_g, e_t;
    FILE *fp=fopen("ecoli1.dat", "r");

    printf("1. triplet tga->[800000, 810000]\n2. triplet tga->[2510000, 2520000]\n");
    printf("--------------------------------------------------------------\n");

    while(!feof(fp)) {
        find[0]=fgetc(fp);
        switch (find[0]) {
            case 'a':
                m_a++;
                break;
            case 'c':
                m_c++;
                break;
            case 'g':
                m_g++;
                break;
            case 't':
                m_t++;
                break;
        }
        
        if(c >=800000 && c <= 810000){
            triplet = 1;
        }else if(c>=2510000 && c<=2520000){
            triplet = 2;
        }
        if((c >=800000 && c <= 810000) || (c>=2510000 && c<=2520000)){
            find[1]=fgetc(fp);
            find[2]=fgetc(fp);
            if(find[0] == 't'){
                if(find[1] == 'g'){
                    if (find[2] == 'a'){
                        printf("%d. Found triplet in position %d-%d\n", triplet, c-2, c);
                        printf("--------------------------------------------------------------\n");
                    }
                }
            }
        }

        if(c >= 800000 && c <= 810000){
            find[3]=fgetc(fp);
            find[4]=fgetc(fp);
            find[5]=fgetc(fp);
            if(find[0] == 't'){
                if(find[1] == 't'){
                    if(find[2] == 'g'){
                        if(find[3] == 'g'){
                            if(find[4] == 'a'){
                                if(find[5] == 't'){
                                    printf("pass\n");
                                    m_ttggat++;
                                }
                            }
                        }
                    }
                }
            }
        }

        fseek(fp, c, SEEK_SET);
        c++;
        ft=ftell(fp);
    }

    fclose(fp);

    e_a = ( (double) m_a / (double) c) * 100;
    e_c = ( (double) m_c / (double) c) * 100;
    e_g = ( (double) m_g / (double) c) * 100;
    e_t = ( (double) m_t / (double) c) * 100;

    printf("--------------------------------------------------------------\n");
    printf("a data base is: %.1lf else %d \n", e_a, m_a);
    printf("c data base is: %.1lf else %d \n", e_c, m_c);
    printf("g data base is: %.1lf else %d \n", e_g, m_g);
    printf("t data base is: %.1lf else %d \n", e_t, m_t);
    printf("--------------------------------------------------------------\n");
    printf("ttggat data base from [800000, 810000] is: %d\n", m_ttggat);
    printf("c=%d all=%d min=%d ftell = %d \n", c, m_a+m_c+m_g+m_t, (m_a+m_c+m_g+m_t)-c, ft);

    return 0;
}