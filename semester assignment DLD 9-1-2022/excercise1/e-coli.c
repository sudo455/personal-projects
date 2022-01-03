// 1) pososto vasewn a, c, g, t apo olo to dat file
// 2) poses fores emfanizetai to tga sto [800000, 810000]U[2510000, 2520000]
// 3) arithmo tou ttggat apo [800000, 810000]

#include <stdio.h>

void c_a(char find_a, int m_a, *in);// απλός εδώ τα γράφω έτσι γιατί με βολεύει
void c_c(char find_c, int m_c, *in);
void c_g(char find_g, int m_g, *in);
void c_t(char find_t, int m_t, *in);
void tga(int i, char ftga[], int m_ftga, *in);
void c_ttggat(int i,char find_ttggat[],int m_ttggat, *in);

int main(void){
    int m_a = 0, m_c = 0, m_g = 0, m_t = 0, m_tga = 0, i = 0;
    double e_a, e_c, e_g, e_t;
    char find_tga[3] = "tga", find_ttggat[6] = "ttggat", find_a = 'a', find_c = 'c', find_g = 'g', find_t = 't';
    FILE *in;
    in = fopen("ecoli1.dat", "r");
    
    while(!feof(in)){ // αν βρεί το EOF στο .dat αρχείο να σταματήσει
        
        c_a(find_a, m_a, in);
        c_c(find_c, m_c, in);
        c_g(find_g, m_g, in);
        c_t(find_t, m_t, in);
        c_tga(i, find_tga, m_tga, in);
        c_ttggat(i, find_ttggat, m_ttggat, in);

        i++
    }

    e_a = (m_a / i) * 100;
    e_c = (m_c / i) * 100;
    e_g = (m_g / i) * 100;
    e_t = (m_t / i) * 100;

    fclose(in);
    return 0;
}

void c_a(char find_a, m_a, *in){
    if(find_a == fgets(find_a,1, in)){
        m_a++;
    }
}

void c_c(char find_c, m_c, *in){
    if(find_c == fgets(find_c,1, in)){
        m_c++;
    }
}

void c_g(char find_g, m_g, *in){
    if(find_g == fgets(find_g,1, in)){
        m_g++;
    }
}

void c_t(char find_t, m_t, *in){
    if(find_t == fgets(find_t,1, in)){
        m_t++;
    }
}

void tga(int i, char ftga[],int m_tga, *in){
    if(((i >= 800000 && i <= 810000) || (i >= 2510000 && i <= 2520000))){ //
        if(fgets(find_tga, 3, in)){
            m_tga++;
        }
    }
}

void ttggat(int i,char ftggat[],int m_ttggat, *in){
    if(i >= 800000 && i <= 810000){
        if (fgets(find_ttggat,6, in)){
            m_ttggat++;
        }
    }
}