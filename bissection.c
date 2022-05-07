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
        double B = 16.47, H = 8.81;
        return B*(H - (4*x)) + (4*x)*((3*x) - H);
    }
    double a = 0;
    double b = 4.41;
    int n = 12;

    //Exemplo 2: Crescimento populacional
    double P(double x){
        double pop = 117417491;
        double porc = 0.25;
        double infec = pop*porc;
        double e = exp(x), n = 117417491,
            lamb = 1.41*pow(10,-10), exp = lamb*(n+1)*x;
        return ((n+1) / (1 + (n*pow(e,-exp)))) - infec;
    }
    double a1 = 0;
    double b1 = 0.2245;
    int n1 = 12;

    //bissection(f, a, b, n)
    //bissection(f, a, b, n);
    /*
    printf("\nexemplo 2\n");
    */
    bissection(P, a1, b1, n1);
}