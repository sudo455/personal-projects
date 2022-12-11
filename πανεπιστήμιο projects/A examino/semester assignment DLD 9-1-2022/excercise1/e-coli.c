// 1) pososto vasewn a, c, g, t apo olo to dat file
// 2) poses fores emfanizetai to tga sto [800000, 810000]U[2510000, 2520000]
// 3) arithmo tou ttggat apo [800000, 810000]

#include <stdio.h>

void find_acgt(int m1, int m2, int m3, int m4,char find){
    if(find == 'a'){
        m1++;
    }else if(find == 'c'){
        m2++;
    }else if(find == 'g'){
        m3++;
    }else if(find == 't'){
        m4++;
    }
}

int main(void){
    int m_a = 0, m_c = 0, m_g = 0, m_t = 0, m_tga1 = 0, m_tga2 = 0, m_ttggat = 0, i = 0, priv = 0, cur = 0, next = cur + 1;
    char data1[4] = "tga", data2[7] = "ttggat", tga[3];
    double e_a, e_c, e_g, e_t;
    FILE *in;
    in = fopen("ecoli1.dat", "r");
    fseek(in, 0, SEEK_SET);
    while(!feof(in)){  // αν βρεί το EOF στο .dat αρχείο να σταματήσει
        
        find_acgt(m_a, m_c, m_g,m_t,fgetc(in));
        
        if(i > 800000 && i < 810000){ //
            if(fgets(data1, 3, in) == tga){
                //printf("pass fn tga \n");
                m_tga1 = m_tga1 + 1;
            }
        }
        if(i > 2510000 && i < 2520000){ //
            if(fgets(data1, 3, in) == data1){
                //printf("pass fn tga \n");
                m_tga2 = m_tga2 + 1;
            }
        }
        
        if(i > 800000 && i < 810000){
            if (fgets(data2, 6, in) == data2){
                //printf("pass fn ttggat \n");
                m_ttggat = m_ttggat + 1;
            }
        }
        i++;
        fseek(in, 1, SEEK_CUR);
        if(i % 1000000 == 0){ 
            printf("i'm doing something...\n");
            printf("ftell =%ld\n", ftell(in));
            printf("i=%d a=%d c=%d g=%d t=%d tga1=%d, tga2=%d tggat=%d, a+c+g+t= %d\n", i, m_a, m_c, m_g, m_t, m_tga1, m_tga2, m_ttggat, m_a+m_c+m_g+m_t);
        }
        //printf("ftell =%ld\n", ftell(in));
        
    }
    fclose(in);
    e_a = ( (double) m_a / (double) m_i) * 100;
    e_c = (m_c / i) * 100;
    e_g = (m_g / i) * 100;
    e_t = (m_t / i) * 100;

    printf("--------------------------------------------------------------\n");
    printf("a data base is: %.3lf else %d \n", e_a, m_a);
    printf("c data base is: %.3lf else %d \n", e_c, m_c);
    printf("g data base is: %.3lf else %d \n", e_g, m_g);
    printf("t data base is: %.3lf else %d \n", e_t, m_t);
    printf("--------------------------------------------------------------\n");
    printf("tga data base from [800000, 810000]U[2510000, 2520000] is: %d \n", m_tga1 + m_tga2);
    printf("tga data base from [800000, 810000] is: %d \n", m_tga1);
    printf("tga data base from [2510000, 2520000] is: %d \n", m_tga2);
    printf("--------------------------------------------------------------\n");
    printf("ttggat data base from [800000, 810000] is: %d\n", m_ttggat);
    printf("i=%d \n", i);
    printf("last value = %d", 4520022);

    
    return 0;
}