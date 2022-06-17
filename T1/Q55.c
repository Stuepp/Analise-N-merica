#include <stdio.h>
#include <math.h>
#define QUANT 7
/*Function to evaluate Li(x)*/

double Li(int i, double x[QUANT], double X);
double Pn(double x[QUANT], double y[QUANT], double X);
void langrange (double x[QUANT], double y[QUANT], double coefs[QUANT]);

int main(void){
    double f(double x){
        //return 1.0 / (1 + 25 * x * x);
        return cos(sin(log(x*x)));
    }
    
    double x[QUANT] = {0.377, 0.682, 1.053, 1.687, 2.1, 2.522, 2.789};
    double y[QUANT];
    
    for (int i = 0; i < QUANT; i++) {
        //y[i] = 1/(1+(25*x[i]*x[i]));
        y[i] = f(x[i]);
    }
    
    double c[QUANT];
    langrange(x,y,c);

    for (int i = 0; i< QUANT; i++)
        printf("%.16f\n", c[i]);
}

void langrange (double x[QUANT], double y[QUANT], double coefs[QUANT]){
   for (int i = 0; i < QUANT; i++){
        double prod = 1;
        for (int j = 0; j < QUANT; j++){
            if (i != j) prod *= x[i] - x[j];
        }
         coefs[i] = y[i] / prod;
    }
}