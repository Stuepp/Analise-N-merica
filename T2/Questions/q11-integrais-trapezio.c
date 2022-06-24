#include <stdio.h>
#include <math.h>

#define LEN 47

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

double trapz_bases_diferentes(double x[], double y[]){ // soma das áreas dos trapézios
    double soma = 0;
    for(int i = 0; i < LEN - 1; i++){
        double altura = y[i] + y[i+1],
            base = x[i+1] - x[i];
        soma += (base * altura) / 2; // formula do trapezio 
    }
    return soma;
}

int main(){
    double func1(double x){
        double g=9.81, m=68.8, cd=0.37;
        return sqrt((g*m) / cd) * tanh(sqrt((g*cd) / m) * x);
    }
    double intervalo[] = {-1.769,1.72};
    //int n = 6683; // número de intervalos
    int n[] = {2, 22, 39, 73, 99, 106, 245, 419, 520, 923, 1146, 8047};
    double x[] = {0.195, 0.295, 0.367, 0.648, 0.759, 0.812, 0.939, 0.999, 1.051, 1.069, 1.214, 1.254, 1.272, 1.334, 1.518, 1.622, 1.714, 1.729, 2.061, 2.147, 2.177, 2.197, 2.412, 2.458, 2.637, 2.64, 2.92, 3.007, 3.011, 3.066, 3.355, 3.583, 3.597, 3.82, 3.848, 3.904, 3.916, 4.095, 4.135, 4.158, 4.168, 4.442, 4.466, 4.52, 4.647, 4.787, 4.804},
        y[] = {1.884, 2.232, 2.457, 2.967, 3.0, 2.987, 2.903, 2.843, 2.784, 2.762, 2.579, 2.528, 2.506, 2.429, 2.23, 2.142, 2.082, 2.073, 2.004, 2.022, 2.031, 2.039, 2.169, 2.208, 2.395, 2.398, 2.749, 2.849, 2.853, 2.907, 2.965, 2.594, 2.557, 1.83, 1.73, 1.535, 1.495, 1.052, 1.012, 1.002, 1.0, 1.686, 1.799, 2.067, 2.662, 2.996, 3.0};
    
   trapz(func1, 0,11.72, 32);
    /*for(int i = 0; i < 12; i++){
        trapz(func1, 0,11.72, 32);
    }*/

    return 0;
}
