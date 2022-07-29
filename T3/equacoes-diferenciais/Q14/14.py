import math

def RK4(f, x0, y0, h, n):
    for _ in range(n):
        m1 = f(x0, y0)
        m2 = f(x0 + (h/2), y0 + (h/2) * m1)
        m3 = f(x0 + (h/2), y0 + (h/2) * m2)
        m4 = f(x0 + h, y0 + h * m3)
        yk = y0 + h * (m1 + 2 * m2 + 2 * m3 + m4)/6
        x0 += h
        y0 = yk
        yield[x0, y0]
    
# modificar valores de r e lambd    
def f(p, t):
    r = 0.1777
    lambd = 0.01483
    k = r * lambd
    return k * (1 - t)

# modificar valor de p0    
t0 = 0
p0 = 0.00122
h = 1
n = 150

r = RK4(f, t0, p0, h, n)

runge = []
for yi in r:
    runge.append(yi[1])
    
# solução exata:
# modificar valores de r, lambd e coef 
def p(t):
    r = 0.1777
    lambd = 0.01483
    k = r * lambd
    # resolver:
    # solve p'(t) = k * (1 - p(t)), p(0) = p0
    # no wolfram, substituindo o valor de p0 dado na questao
    coef = 0.99878
    return 1 - coef * math.exp(-k*t)
    
for i in range(150):
    print(f"{runge[i]}, {abs(runge[i] - p(i))},")

"""
No livro Looking at History Through Mathematics, Rashevsky [Ra], p. 103-110, considera um modelo
para um problema envolvendo a produção de rebendes na sociedade. Considere uma sociedade com x(t)
indivíduos no instante t, em anos, e suponha que todo rebelde que se acasale com outro rebelde 
tenha filhos também rebeldes, enquanto uma proporção fixa r de todos os filhos de outros tipos
de acasalamento também seja rebelde. Se for suposto que as taxas de nascimento e mortalidade
para todos os indivíduos são as constantes λ e μ, respectivamente, e se não rebeldes e rebeldes
dx(t)dt=(λ−μ)x(t)edxn(t)dt=(λ−μ)xn(t)+rλ(x(t)−xn(t)) ,
em que xn(t) denota o número de rebeldes na população no instante t.
Suponha que a variável p(t)=xn(t)/x(t) seja introduzida para representar a proporção de rebeldes na sociedade no instante t. Neste caso, as equações diferenciais acima podem ser combinadas e simplificadas na única equação diferencial
dp(t)dt=rλ(1−p(t)).
Considerando p(t0)=p0, com t0=0, p0=0.00122, λ=0.01483, μ=0.00601 e r=0.1777, use o método de Runge-Kutta de ordem 4 para encontrar aproximações para a solução p(t) nos instantes tk=t0+kh, onde k=1,2,…,150 e h=1 ano. Além disso, encontre a solução algébrica exata p(t) e calcule os erros |p(tk)−pk|, k=1,2,…,150. Por fim, reflita sobre o que acontecerá com a taxa de rebeldes nessa sociedade depois de alguns séculos.se acasalam aleatoriamente, o problema pode ser expresso pelas equações diferenciais
.....
dx(t)dt=(λ−μ)x(t)edxn(t)dt=(λ−μ)xn(t)+rλ(x(t)−xn(t)) ,
em que xn(t) denota o número de rebeldes na população no instante t.
Suponha que a variável p(t)=xn(t)/x(t) seja introduzida para representar a proporção de rebeldes na sociedade no instante t. Neste caso, as equações diferenciais acima podem ser combinadas e simplificadas na única equação diferencial
dp(t)dt=rλ(1−p(t)).
Considerando p(t0)=p0, com t0=0, p0=0.00122, λ=0.01483, μ=0.00601 e r=0.1777,
use o método de Runge-Kutta de ordem 4 para encontrar aproximações para a solução p(t) nos instantes
tk=t0+kh, onde k=1,2,…,150 e h=1 ano. Além disso, encontre a solução algébrica exata p(t) e calcule
os erros |p(tk)−pk|, k=1,2,…,150. Por fim, reflita sobre o que acontecerá com a taxa de rebeldes
nessa sociedade depois de alguns séculos.
"""