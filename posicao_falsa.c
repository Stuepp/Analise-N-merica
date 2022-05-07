#include <stdio.h>
#include <math.h>

void false_position(double (*f)(double),double a,double b,int n){
    double fa = f(a);
    double fb = f(b);
    if(fa * fb >= 0){
        printf("O Teorema de Bolzano não sabe dizer se existe raiz para f no intervalo [%.16f, %.16f]",a,b);
        return;
    }else {
        double x;
        for(int i =0;i<n;i++){
            x = (a *fb - b * fa) / (fb - fa);
            printf("x_%d = %.16f\n", i+1,x);
            double fx = f(x);
            if(fx == 0){
                printf("Encontramos uma raiz para f, ela é x = %.16f",x);
                return;
            }
            if(fa * fx < 0){
                b = x;
                fb = fx;
            }else{
                a = x;
                fa = fx;
            }
        }
    }
}

int main(){
    double f(double x){
        double B = 16.47, H = 8.81;
        return B*(H - (4*x)) + (4*x)*((3*x) - H);
    }
    //intervalo inicial
    double a = 0;
    double b = 4.41;

    int n = 11; // número de iterações

    false_position(f,a,b,n);
}