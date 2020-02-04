
#include <iostream>
#include <math.h>
#include <stdio.h>
#include <fstream>

using namespace std;

#define h 0.5 // tamaño de paso
#define A 0 //punto inicial
#define B  50 //punto final
#define pi 3.1416


double f(double t, double x){
	double F,a,b,w;
	F =  120; //intensidad de la fuerza (N)
	a =  -4; // constante
	b =  -4; // constante
	w = 2*pi; //periodo de la fuerza F
	return F*cos(w*t)-(a*x)-(b*pow(x,3));
}

double g(double y){
	return y;
}

int main(){

 ofstream file;
 file.open("datos.dat");

 double t[200];

 double x[200];
 double y[200];
 y[0]=0.15;;  //condicion inicial para x(0), posicion en t=0

 double d[200];
 double z[200];
 z[0] = 0; //condicion inicial para g, y= x'(0)=0

 for (int i=1; i <= B; i++){
 float k1,k2,k3,k4,l1,l2,l3,l4;
 k1 = h*g(x[i]);
 l1 = h*f(t[i],d[i]);

 k2 = h*g(x[i] + l1/2);
 l2 = h*f(t[i] + h/2, d[i] + k1/2);

 k3 = h*g(x[i] + l2/2);
 l3 = h*f(t[i] + h/2, d[i] + k2/2);

 k4 = h*g(x[i] + l3);
 l4 = h*f(t[i] + h, d[i] + k3);

 y[i + 1] = y[i] + (k1 + 2*k2 + 2*k3 + k4)/6;
 z[i + 1] = z[i] + (l1 + 2*l2 + 2*l3 + l4)/6; 

 file<< i <<"  "<< y[i]<<"\n"<<endl;
 }
 
 file.close();
 return 0;
}