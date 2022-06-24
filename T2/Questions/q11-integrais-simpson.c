#include <stdio.h>
#include <math.h>

#define LEN 45

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

void simps_y(double x[], double y[]){
    double soma = 0;
    for(int i = 0; i < LEN - 2; i+=2){
        soma += ((x[i+1] - x[i]) / 3.0) * (y[i] + 4 * y[i+1] + y[i+2]);
    }
    printf("%.16f\n", soma);
}

int main(){
    double func(double x){
        double g=9.81, m=68.8, cd=0.37;
        return sqrt((g*m) / cd) * tanh(sqrt((g*cd) / m) * x);
    }
    double intervalo[] = {0,11.72};
    int n[] = {6,14,40,72,84,114,130,154,188,230,488}; // nº de intervalos

    double x[] = {0.019, 0.0345, 0.05, 0.087, 0.124, 0.3595, 0.595, 0.5975, 0.6, 0.6105, 0.621, 0.763, 0.905, 1.026, 1.147, 1.3145, 1.482, 1.494, 1.506, 1.7115, 1.917, 1.9225, 1.928, 2.055, 2.182, 2.3405, 2.499, 2.4995, 2.5, 2.5915, 2.683, 2.8675, 3.052, 3.4535, 3.855, 3.9545, 4.054, 4.208, 4.362, 4.5005, 4.639, 4.6935, 4.748, 4.7535, 4.759},
        y[] = {1.295, 1.339, 1.386, 1.505, 1.631, 2.435, 2.92, 2.923, 2.925, 2.936, 2.946, 2.999, 2.932, 2.813, 2.665, 2.453, 2.265, 2.253, 2.242, 2.083, 2.007, 2.006, 2.005, 2.003, 2.033, 2.116, 2.246, 2.247, 2.247, 2.343, 2.45, 2.684, 2.894, 2.857, 1.705, 1.372, 1.119, 1.013, 1.353, 1.969, 2.63, 2.826, 2.955, 2.963, 2.971};

    //simps_y(x, y);
    simps(func,intervalo[0],intervalo[1],16);

    /*for(int i = 0; i < 11; i++){
        simps(func,intervalo[0],intervalo[1],n[i]);
    }*/

    return 0;
}
