Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@sudo455 
skiado
/
OOP
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
OOP/labs/02/02_01.cpp
@skiado
skiado Add files via upload
Latest commit b6cfdd9 16 days ago
 History
 1 contributor
52 lines (42 sloc)  763 Bytes
  
#include <iostream>

using namespace std;

void p_line();
void p_line(char c);
void p_line(char c, int num);
void p_line(char c1,char c2, int num);

int main(){

	cout << "p_line()" << endl;
	p_line();
	cout <<  "p_line(\'*\')" << endl;
	p_line('*');
	cout << "p_line(\'#\',30)" << endl;
	p_line('#',30);
	cout <<  "p_line(\'-\',\'+\',20)" << endl;
	p_line('-','+',20);
	return 0;
}

void p_line(){
	for(int i=0;i<15;i++){
		cout << '-';
	}
	cout << endl;
}

void p_line(char c){
	for(int i=0;i<15;i++){
		cout << c;
	}
	cout << endl;
}

void p_line(char c, int num){
	for(int i=0;i<num;i++){
		cout << c;
	}
	cout << endl;
}

void p_line(char c1,char c2, int num){
	for(int i=0;i<num;i++){
		cout << c1 << c2 << c1;
	}
	cout << endl;
}

// g++ -o 01 02_01.cpp
	
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Loading complete