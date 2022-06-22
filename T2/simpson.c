#include <stdio.h>
#include <math.h>

void simps(double(*f)(double), double a, double b, int n){
    if(n % 2 != 0){
        printf("O número de subintervalos deve ser par\n");
        return;
    }
    int numParabolas = n / 2;
    double soma = 0;
    double h = (double)(b - a) / (double) n;
    for(int k = 0; k < numParabolas; k++){
        double x0 = a + (2 * k) * h;
        double x1 = a + (2 * k + 1) * h;
        double x2 = a + (2 * k + 2) * h;
        soma += (f(x0) + 4 * f(x1) + f(x2));
    }
    soma *= (h/3.0);
    printf("Area aprox: %.16f\n", soma);
}

int main(){
    double func(double x){
        return sqrt(1 + pow(cos(x),2));
    }
    double intevalo[] = {-1.648, 1.589};
    int n[] = {6,14,40,72,84,114,130,154,188,230,488}; // nº de intervalos

    for(int i = 0; i < 11; i++){
        simps(func,intevalo[0],intevalo[1],n[i]);
    }

    return 0;
}