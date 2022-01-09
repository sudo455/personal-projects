#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *fp, *results;
    long count=0,counta=0,countc=0,countg=0,countt=0, pos1=-1, pos2=-1;
    int c, c1, c2, c3, c4, c5, c6;

    fp = fopen( "ecoli1.dat", "r" );

    c=fgetc(fp);
    while (c != EOF) {
        ++count;
        if (c=='a')
            ++counta;
        if (c=='c')
            ++countc;
        if (c=='g')
            ++countg;
        if (c=='t')
            ++countt;
        c=fgetc(fp);
    }

    fclose(fp);
    printf("Pososto a=%f\nPososto c=%f\nPososto g=%f\nPososto t=%f\n", (float)counta/count * 100, (float) countc/count*100, (float) countg/count*100, (float) countt/count*100);

    results = fopen ("results.txt", "w");

    count = 0;
    fp = fopen( "ecoli1.dat", "r" );
    fprintf (results, "tga -> 800000 - 810000\n");

    c1 = fgetc(fp);
    c2 = fgetc(fp);
    c3 = fgetc(fp);
    while (c1 != EOF && c2 != EOF && c3 != EOF) {
        if (count >= 800000 && count <= 809998)
            if (c1 == 't' && c2 == 'g' && c3 == 'a')
                fprintf (results, "%ld\n", count);
        count+=1;
        c1 = c2;
        c2 = c3;
        c3=fgetc(fp);
    }
    fclose(fp);

    count = 0;
    fp = fopen( "ecoli1.dat", "r" );
    fprintf (results,"tga -> 2510000 - 2520000\n");

    c1 = fgetc(fp);
    c2 = fgetc(fp);
    c3 = fgetc(fp);
    while (c1 != EOF && c2 != EOF && c3 != EOF) {
        if (count >= 2510000 && count <= 2519998)
            if (c1 == 't' && c2 == 'g' && c3 == 'a')
                fprintf (results,"%ld\n", count);
        count+=1;
        c1 = c2;
        c2 = c3;
        c3=fgetc(fp);
    }
    fclose(fp);

    count = 0;
    fp = fopen( "ecoli1.dat", "r" );
    fprintf (results,"ttggat -> 800000 - 810000\n");

    c1 = fgetc(fp);
    c2 = fgetc(fp);
    c3 = fgetc(fp);
    c4 = fgetc(fp);
    c5 = fgetc(fp);
    c6 = fgetc(fp);
    while (c1 != EOF && c2 != EOF && c3 != EOF && c4 != EOF && c5 != EOF && c6 != EOF) {
        if (count >= 800000 && count <= 809995)
            if (c1 == 't' && c2 == 't' && c3 == 'g' && c4 == 'g' && c5 == 'a' && c6 == 't') {
                fprintf (results, "%ld\n", count);
                if (pos1 == -1)
                    pos1 = count;
                else
                    pos2 = count;
            }
        count+=1;
        c1 = c2;
        c2 = c3;
        c3 = c4;
        c4 = c5;
        c5 = c6;
        c6=fgetc(fp);
    }
    fprintf(results,"%ld", pos2 - pos1);
    fclose(fp);

    fclose(results);
    return 0;
}
