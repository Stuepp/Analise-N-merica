#include <stdio.h>
#include <math.h>

void trapz(double(*f)(double), double a, double b, int n){
    double 
    soma = 0,
    h = (double)(b - a) / (double)n;
    for(int k = 1; k < n; k++){
        soma += f(a + k * h);
    }
    soma *= 2;
    soma += f(a) + f(b);
    //soma += f(b);
    soma *= (h / 2.0);
    printf("\nArea aprox: %.16f", soma);
}

int main(){
    double func1(double x){
        return exp(-x*x);
    }
    double 
        a = 0,
        b = 1;
    int n = 10; // número de intervalos

    trapz(func1, a, b, n);
    return 0;
}