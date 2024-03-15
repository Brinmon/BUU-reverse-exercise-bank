// #include <iostream>
#include<stdio.h>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

void decry_tea(unsigned int* text, unsigned int* key){
	unsigned int delta = 0x9e3779b9;  // -delta
	unsigned int sum = 0xC6EF3720; //   v16
	unsigned int v1 = text[1];
	unsigned int v0 = text[0];

	for (int i = 0; i < 32; i ++){
		v1-=((v0<<4)+key[2])^(v0+sum)^((v0>>5)+key[3]);
		v0-=((v1<<4)+key[0])^(v1+sum)^((v1>>5)+key[1]);
		sum -= delta;
		//printf("%d\n",sum);
	}
	text[1] = v1;
	text[0] = v0;
	
}

void encrypt(unsigned int* v,unsigned int* k){
	unsigned int v0=v[0],v1=v[1],sum=0,i;
	unsigned int delta=0x9e3779b9;
	unsigned int k0=k[0],k1=k[1],k2=k[2],k3=k[3];
	for(i = 0; i < 32; i++){
		sum += delta;
		v0 += ((v1<<4)+k0)^(v1+sum)^((v1>>5)+k1);
		v1 += ((v0<<4)+k2)^(v0+sum)^((v0>>5)+k3);
	}
	v[0]=v0;
	v[1]=v1;
}


int main(int argc, char** argv) { 
	unsigned int key[] = {3735928559u, 590558003u, 19088743u, 4275878552u};
	unsigned int text1[] = {0xf1f5d29b ,0x6e4414ec};
	//unsigned int* text1 = (unsigned int*)a;


	decry_tea(text1, key); 
	//encrypt(text0, key);
	printf("%x %x", text1[0], text1[1]);
	printf("\n\n");
	for (int i = 0 ; i < 8; i ++){
		printf("%c", *((char*)text1 + i));
	}
	return 0;
}