#​include​ ​<​stdio.h​> 
#​include​ ​<​stdbool.h​> 
int​ ​main​(​void​) { 
    ​int​ m_a=​0​, m_c=​0​, m_g=​0​, ​m_t​=​0​, m_ttggat=​0​, c=​0​, offset=​0​; 
    ​char​ find_tga[​10000​][​2​]; 
    ​double​ e_a, e_c, e_g, ​e_t​; 
    FILE *fp=​fopen​(​"​ecoli1.dat​"​, ​"​r​"​); 
    ​printf​(​"​1. triplet tga->[800000, 810000]​\n​2. triplet tga->[2510000, 2520000]​\n​"​); 
    ​printf​(​"​--------------------------------------------------------------​\n​"​); 
    ​while​(!​feof​(fp)) { 
         
        ​switch​ (​fgetc​(fp)) { 
            ​case​ ​'​a​'​: 
                m_a++; 
                ​break​; 
            ​case​ ​'​c​'​: 
                m_c++; 
                ​break​; 
            ​case​ ​'​g​'​: 
                m_g++; 
                ​break​; 
            ​case​ ​'​t​'​: 
                ​m_t​++; 
                ​break​; 
        } 
         
        ​if​(​ftell​(fp) >=​800000​ && ​ftell​(fp) <= ​810000​){ 
            offset = offset - ​1​; 
            ​if​(​fgetc​(fp) == ​'​t​'​){ 
                offset = offset - ​1​; 
                ​if​(​fgetc​(fp) == ​'​g​'​){ 
                    offset = offset - ​1​; 
                    ​if​ (​fgetc​(fp) == ​'​a​'​){ 
                        offset = offset - ​1​; 
                        ​printf​(​"​1. Found triplet in position ​%ld​-​%ld​\n​"​,​ftell​(fp)-​2​, ​ftell​(fp)); 
                        ​printf​(​"​--------------------------------------------------------------​\n​"​); 
                    } 
                } 
            } 
            ​fseek​(fp, offset,SEEK_CUR); 
            offset = ​0​; 
        } 
         
        ​if​(​ftell​(fp)>=​2510000​ && ​ftell​(fp)<=​2520000​){ 
            ​if​(​fgetc​(fp) == ​'​t​'​){ 
                offset = offset - ​1​; 
                ​if​(​fgetc​(fp) == ​'​g​'​){ 
                    offset = offset - ​1​; 
                    ​if​ (​fgetc​(fp) == ​'​a​'​){ 
                        offset = offset - ​1​; 
                        ​printf​(​"​2. Found triplet in position ​%ld​-​%ld​\n​"​, ​ftell​(fp)-​2​, ​ftell​(fp)); 
                        ​printf​(​"​--------------------------------------------------------------​\n​"​); 
                    } 
                } 
            } 
            ​fseek​(fp, offset,SEEK_CUR); 
            offset = ​0​; 
        } 
         
        ​if​(​ftell​(fp)>=​800000​ && ​ftell​(fp)<=​810000​){ 
            ​if​(​fgetc​(fp) == ​'​t​'​){ 
                offset = offset - ​1​; 
                ​if​(​fgetc​(fp) == ​'​t​'​){ 
                    offset = offset - ​1​; 
                    ​if​(​fgetc​(fp) == ​'​g​'​){ 
                        offset = offset - ​1​; 
                        ​if​(​fgetc​(fp) == ​'​g​'​){ 
                            offset = offset - ​1​; 
                            ​if​(​fgetc​(fp) == ​'​a​'​){ 
                                offset = offset - ​1​; 
                                ​if​(​fgetc​(fp) == ​'​t​'​){ 
                                    offset = offset - ​1​; 
                                    m_ttggat++; 
                                } 
                            } 
                        } 
                    } 
                } 
            } 
            ​fseek​(fp, offset,SEEK_CUR); 
            offset = ​0​; 
        } 
        c = ​ftell​(fp); 
    } 
    ​fclose​(fp); 
    e_a = ( (​double​) m_a / (​double​) c) * ​100​; 
    e_c = ( (​double​) m_c / (​double​) c) * ​100​; 
    e_g = ( (​double​) m_g / (​double​) c) * ​100​; 
    ​e_t​ = ( (​double​) ​m_t​ / (​double​) c) * ​100​; 
    ​printf​(​"​--------------------------------------------------------------​\n​"​); 
    ​printf​(​"​a data base is: ​%.3lf​ else ​%d​ ​\n​"​, e_a, m_a); 
    ​printf​(​"​c data base is: ​%.3lf​ else ​%d​ ​\n​"​, e_c, m_c); 
    ​printf​(​"​g data base is: ​%.3lf​ else ​%d​ ​\n​"​, e_g, m_g); 
    ​printf​(​"​t data base is: ​%.3lf​ else ​%d​ ​\n​"​, ​e_t​, ​m_t​); 
    ​printf​(​"​--------------------------------------------------------------​\n​"​); 
    ​printf​(​"​ttggat data base from [800000, 810000] is: ​%d​\n​"​, m_ttggat); 
    ​printf​(​"​c=​%d​ all=​%d​ min=​%d​ ​\n​"​, c, m_a+m_c+m_g+​m_t​, (m_a+m_c+m_g+​m_t​)-c); 
    ​return​ ​0​; 
}