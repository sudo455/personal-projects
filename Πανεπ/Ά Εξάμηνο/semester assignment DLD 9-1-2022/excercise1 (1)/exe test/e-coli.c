#include <stdio.h>
#include <stdbool.h>

int main(void) {
    int m_a=0, m_c=0, m_g=0, m_t=0, c=0, cc, i, m_f_b_ttggat = 0;
    char find[6];
    double e_a, e_c, e_g, e_t;
    bool found = false;
    FILE *fp=fopen("ecoli1.dat", "r");

    printf("1. triplet tga->[800000, 810000]\n2. triplet tga->[2510000, 2520000]\n");
    printf("--------------------------------------------------------------\n");

    find[0] = fgetc(fp);

    while(!feof(fp)) {

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
        
        if(ftell(fp) >= 800000 && ftell(fp) <= 810000){
            if(find[1] == NULL && find[2] == NULL){
                find[1] = fgetc(fp);
                find[2] = fgetc(fp);
            }
            if(find[0] == 't'){
                if(find[1] == 'g'){
                    if (find[2] == 'a'){
                        printf("1. Found triplet in position %ld-%ld\n",ftell(fp)-2, ftell(fp));
                        printf("--------------------------------------------------------------\n");
                    }
                }
            }
            if(find[3] == NULL && find[4] == NULL && find[5] == NULL){
                find[3] = fgetc(fp);
                find[4] = fgetc(fp);
                find[5] = fgetc(fp);
                fseek(fp, -6, SEEK_CUR);
            }
            cc = 5;
            if(find[0] == 't'){
                if(find[1] == 't'){
                    if(find[2] == 'g'){
                        if(find[3] == 'g'){
                            if(find[4] == 'a'){
                                if(find[5] == 't'){
                                    found = !found;
                                }
                            }
                        }
                    }
                }
            }

            if(found){
                m_f_b_ttggat++;
            }

            for(i = 0; i < cc; i++){
                find[i] = find[i+1];
            }
            find[cc] = fgetc(fp);
        }

        if(ftell(fp) == 2509999){
            find[1] = NULL;
            find[2] = NULL;
        }

        if(ftell(fp)>=2510000 && ftell(fp)<=2520000){
            if(find[1] == NULL && find[2] == NULL){
                find[1] = fgetc(fp);
                find[2] = fgetc(fp);
                fseek(fp, -3, SEEK_CUR);
            }
            cc = 2;
            if(find[0] == 't'){
                if(find[1] == 'g'){
                    if (find[2] == 'a'){
                        printf("2. Found triplet in position %ld-%ld\n", ftell(fp)-2, ftell(fp));
                        printf("--------------------------------------------------------------\n");
                    }
                }
            }
            for(i = 0; i < cc; i++){
                find[i] = find[i+1];
            }
            find[cc] = fgetc(fp);
        }
        if(!((ftell(fp) >=800000 && ftell(fp) <= 810000) || (ftell(fp)>=2510000 && ftell(fp)<=2520000))){
            find[0] = fgetc(fp);

        }
        
        c = ftell(fp);
    }

    fclose(fp);

    e_a = ( (double) m_a / (double) c) * 100;
    e_c = ( (double) m_c / (double) c) * 100;
    e_g = ( (double) m_g / (double) c) * 100;
    e_t = ( (double) m_t / (double) c) * 100;

    printf("a data base is: %.3lf\n", e_a);
    printf("c data base is: %.3lf\n", e_c);
    printf("g data base is: %.3lf\n", e_g);
    printf("t data base is: %.3lf\n", e_t);
    printf("--------------------------------------------------------------\n");
    printf("number of bases acgt between 2 ttggat data base from [800000, 810000] is: %d\n", m_f_b_ttggat);
    printf("c = %d all_acgt = %d off_by = %d \n", c, m_a+m_c+m_g+m_t, c-(m_a+m_c+m_g+m_t));

    return 0;
}