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
        return sqrt(sin(cos(log(x*x + 1) + 2) + 3) + 4);
    }
    double intervalo[] = {-1.769,1.72};
    //int n = 6683; // número de intervalos
    int n[] = {2, 22, 39, 73, 99, 106, 245, 419, 520, 923, 1146, 8047};
    for(int i = 0; i < 12; i++){
        trapz(func1, intervalo[0], intervalo[1], n[i]);
    }
    return 0;
}