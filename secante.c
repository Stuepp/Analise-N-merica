#include <stdio.h>
#include <math.h>

void secante(double (*f)(double), double x0, double x1, int n){
    double fx0 = f(x0);
    double fx1 = f(x1);
    if(fx0 == fx1){
        printf("Escolha outras estimativas iniciais");
    } else {
        for(int i =0; i<n;i++){
            double x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0);

            fx0 = f(x1);
            fx1 = f(x2);
            if(fx0 == fx1){
                printf("x_%d = %.16f (preisei parar)",i+2,x2);
                return;
            }else{
                printf("x_%d = %.16f\n",i+2,x2);
                x0 = x1;
                x1 = x2;
            }
        }
    }
}

int main(){
    double f(double x){
        double L = 8.58, r = 3.22, V = 103.9;
        return L*((0.5*M_PI*pow(r,2)) - ((pow(r,2))*asin(x/r)) - (x*sqrt(pow(r,2) - pow(x,2)))) - V;
    }

    double x0 = 0.34;
    double x1 = 2.81;
    int n = 5;

    secante(f, x0, x1, n);
}