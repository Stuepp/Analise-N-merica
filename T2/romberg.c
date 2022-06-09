#include <stdio.h>
#include <math.h>

// 4 poisa primeira coluna deve ter 'error_order/2' elementos
#define error_order 16
#define  numElemFristCol 8

// método dos trapezios
double trapz(double (*f)(double), double a, double b, int n){
    double soma = 0;
    double h = (double) (b - a) / (double) n;
    for(int i = 1; i<n; i++){
        double xi = a + i * h;
        soma += f(xi);
    }
    soma *= 2;
    soma += f(a);
    soma += f(b);
    soma *= (0.5 * h);
    return soma;
}

void romberg(double array[]){
    // i = 0  está calculando a coluna F2
    int numCols = error_order / 2.0 - 1;
    for(int i = 0; i < numCols; i++){
        for(int j = 0; j < numCols; j++){
            double numer = pow(2, (i + 1) * 2) * array[j + 1] - array[j];
            double denom = pow(2, (i + 1) * 2) - 1;
            array[j] = numer / denom;
        }
    }
    printf("\nAprox O(h^%d)=%.16f", error_order, array[0]);
}

    // exemplo
    // aroximar a integral exp(-x*x), de 0 a 1
double f(double x){ // func
        return exp(-x*x);
}

int main(){
    double a = 0;
    double b = 1;
    double h = 0.5;
    int n = (b - a) / h;
    double coluna_F1[numElemFristCol] = {};
    for(int i = 0; i < numElemFristCol; i++){
        coluna_F1[i] = trapz(f, a, b,pow(2, i) * n);
        printf("\n%.16f", coluna_F1[i]);
    }
    romberg(coluna_F1);

    return 0;
}