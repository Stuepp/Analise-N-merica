def true_euler(f, k, x0, y0, h, n):
    for i in range(n):
        y0 += h * f(x0, y0, k)
        x0 += h        
        #print(f'x_{i + 1}={x0} e y_{i+1}={y0}')
    print(f'{y0}')

if __name__ == '__main__':
    def f(x, y, k):
        return k*y + 34494
    
    x0, y0 = 0.0, 1141534 # x0 = t, y0 = individuos
    h = 0.0625
    k = 0.0602
    n = int(1 / h)
    true_euler(f, k, x0, y0, h, n)