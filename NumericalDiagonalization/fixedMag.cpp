#include <iostream>
#include <fstream>
#include <cmath>
#include <ctime>
#include <string>
#include <bitset>
#include <cstdio>
#include <cmath>


const unsigned long int bits = 8;

unsigned long int ieor(int integer, int pos1, int pos2);
unsigned long int cycleBits(int integer);
int btest(int integer, int position);
void Deallocate(float **H, int N);
float** Allocate(int N);
long int fat(int N);
int bitSum(int integer);
int findState(int *sa,int s, int dim);
void representative(unsigned int s, unsigned int &r, unsigned int &l);

int main(){
	int N, dim, nUp, M;
	int i, j, aux;
	int state, s, pos;
	int *sa;

	float **H;

	std :: ofstream outPut;
	outPut.open("Hamiltonian.txt");

	N = 3;
	dim = pow(2, N);
	
	H = Allocate(dim);
	sa = new int [dim];
	aux = 0;
	for(nUp=1; nUp<=N; nUp++){
		for(i=0; i<dim; i++){
			if(bitSum(i) == nUp){
				aux = aux + 1;
				sa[aux] = i;	
			}
		}
	}
	for(i=0; i<dim; i++){
		std :: cout<<sa[i]<<"\n";
	}
	
	for(state=0; state<dim; state++){
		for(i=0; i<N; i++){
			j = (i+1)%N;
			pos = findState(sa, state, dim);
			if(btest(sa[state], i) == btest(sa[state], j)){
				H[pos][pos] = H[pos][pos] + 1./4.;
			}else{
				H[pos][pos] = H[pos][pos] - 1./4.;
				s = ieor(sa[state], i, j);
				aux = findState(sa, s, dim);
				H[pos][aux] = H[pos][aux] + 1./2.;
			}
		}
	}
	

	for(i=0; i<dim; i++){
		for(j=0; j<dim; j++){
			if( std :: abs(H[i][j]) > 0.00000001){
            outPut << i << "    " << j << "    " << H[i][j] << "\n ";
			}
		}
    }

	Deallocate(H, dim);
	delete [] sa;

	outPut.close();
}


void representative(unsigned int s, unsigned int &r, unsigned int &l){
	int t=s;
    l=0;
    r=s;
    for(int i = 0; i<4-1; i++){
        t = cycleBits(t);
        if( t <  r){
            r = t;
            l = i;
        }   
	}   
}

unsigned long int cycleBits(int integer){
	char aux0, aux1;
	char binary1[bits];
	std :: string binary = std::bitset<bits>(integer).to_string();
	for(int i=0; i<bits; i++){
		binary1[(i+1) % bits] = binary[i];
	}
	unsigned long int decimal = std::bitset<bits>(binary1).to_ulong();
	return decimal;
}

int findState(int *sa,int s, int dim){
	for(int i=0; i<dim; i++){
		if( sa[i] == s){
			return i;
		}
	}
	return -1;
}

long int fat(int N){
	long int acum;
	acum = 1;
	for(int i=N; i>0; i--){
		acum = acum*i	;
	}
	return acum;
}

void Deallocate(float **H, int N){
	for(int i=0; i<N; i++){
		delete [] H[i];
	}
	delete [] H;
}

float** Allocate(int N){
	float **H;
	H = new float*[N];
	for(int i=0; i<N; i++){
		H[i] = new float[N];
	}
	for(int i=0; i<N; i++){
		for(int j=0; j<N; j++){
			H[i][j] = 0.0;
		}
	}
	return H;
}
int bitSum(int integer){
	int sum, ss;
	sum = 0;
	ss = integer;
	while( ss != 0){
		if(ss % 2 == 1){
			ss = ss/2;
			sum ++;
		}else{
			ss = ss/2;
		}

	}
	return sum;
}

int btest(int integer, int position){
	std :: string binary = std::bitset<bits>(integer).to_string(); 
	return binary[bits - position - 1] <<'\n';
}

unsigned long int ieor(int integer, int pos0, int pos1){
	std :: string binary = std::bitset<bits>(integer).to_string(); 
	if(binary[bits - pos0 - 1] == '1'){
		binary[bits - pos0 - 1] = '0';
	}else if(binary[bits - pos0 - 1] == '0'){
		binary[bits - pos0 - 1] = '1';
	}

	if(binary[bits - pos1 - 1] == '1'){
		binary[bits - pos1 - 1] = '0';
	}else if(binary[bits - pos1 - 1] == '0'){
		binary[bits - pos1 - 1] = '1';
	}
	unsigned long decimal = std::bitset<bits>(binary).to_ulong();
	return decimal;
}

