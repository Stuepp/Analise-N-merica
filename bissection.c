#include <stdio.h>
#include <math.h>

//#define M_E 2.71828182845904523536028747135266250

void bissection(double (*f)(double), double a, double b, int n){
    if(f(a) * f(b) >= 0){
        printf("Não é possível usar Bolzano para garantir a existência de uma raiz em [%4.f,%4.f]", a, b);
    } else {
        for(int i = 0; i < n; i++){
            double m = 0.5 * (a + b);
            printf("x_%d = %.16f\n", i+1, m);
            if(f(m) == 0){
                printf("Yay você encontrou a raiz r = %.16f", m);
            } else {
                if(f(a) * f(m) < 0){
                    b = m;
                } else {
                    a = m;
                }
            }
        }
    }
}

int main(){
    //Exemplo 1: f(x) = e^x -2x² + x - 1.5 [0.16894,0.87585]
    double f(double x){
        return pow(M_E,x) + -2*(x*x) + x - 1.5;
    }
    double a = 0.16894;
    double b = 0.87585;
    int n = 12;

    //Exemplo 2: Crescimento populacional
    double P(double x){
        double e = exp(x);
        return e * 1000000 + (537142 / x) * (e - 1) - 1863961;
    }
    double a1 = 0.001;
    double b1 = 2;
    int n1 = 20;

    //bissection(f, a, b, n)
    bissection(f, a, b, n);
    /*
    printf("\nexemplo 2\n");
    bissection(P, a1, b1, n1);
    */
}