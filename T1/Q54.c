#include <stdio.h>
#define QUANT 8
/*Function to evaluate Li(x)*/

double Li(int i, double x[QUANT], double X);
double Pn(double x[QUANT], double y[QUANT], double X);
void langrange (double x[QUANT], double y[QUANT], double coefs[QUANT]);

int main(void){
    double f(double x){
        return 1.0 / (1 + 25 * x * x);
    }
    
    double x[QUANT] = {-1.305, -0.477, 0.611, 1.574, 3.146, 4.023, 5.278, 6.728};
    double y[QUANT] = {0.808, 0.965, 0.954, 0.697, -0.452, -0.95, -0.656, 0.624};
    
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