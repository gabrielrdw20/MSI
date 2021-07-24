 # Code authors' usernames:
 # gabrielrdw20 
 # krzysztoftora
 # "\n"
 # Code in Python
 # "\n\n"
 # **Zrównoleglony algorytm ewolucyjny (1+1)** / **Parallel evolutionary algorithm (1+1)**
 # Poszukiwanie maksimum lokalnego w funkcji $f(x_1, x_2) = -x_1^2 - x_2^2 +2$ dla $-2 \le x_1 \le 2$, $-2 \le x_2 \le 2$. 
 # Parametry algorytmu: $m$ = 10, $c_1$ = 0,82, $c_2$ = 1,20
import numpy as np
import random
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from math import exp, expm1

sigma = 1.0
sigma_min = 0.000001
m = 10

def function(x):
    return (-1 * (x[0] - 0.5) ** 2 - (x[1] + 0.5) ** 2 + 2 - x[0]*x[1] * exp(1e-5))

x = np.outer(np.linspace(-1.5, 2.5, 100), np.ones(100))
y = x.copy().T - 1
z = function([x,y])

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')
ax.set(title='f(x1, x2)', xlabel='x1', ylabel='x2')
plt.show()

c1 = 0.82
c2 = 1.20
threshold = 0.2
result = 0
n = 0
output_box = []

def choice(phi, sigma):
    if phi < threshold:
        return c1 * sigma
    elif phi > threshold:
        return c2 * sigma
    else:
        return sigma
    
def evolutionary(sigma, sigma_min, m, function, x1, x2, y1, y2):
    # maksimum lokalne funkcji
    x = [random.uniform(x1, x2), random.uniform(y1, y2)];
    while sigma > sigma_min:
        phi = 0 
        for i in range(m):
            N = [np.random.normal(0,1), np.random.normal(0,1)];
            y = [x[0] + sigma * N[0], x[1] + sigma * N[1]];
            if function(y) >= function(x):
                x = y
                phi += 1/m
        sigma = choice(phi, sigma)
    return x


while n < 50:
    n += 1
    
    a = evolutionary(sigma, sigma_min, m, function, -2, 2, -2, 2)
    b = evolutionary(sigma, sigma_min, m, function, -2, 2, -2, 2)
    d = evolutionary(sigma, sigma_min, m, function, -2, 2, -2, 2)
    
    func_a = function(a)
    func_b = function(b)
    func_d = function(d)
    
    check = max(func_a, func_b, func_d)
    
    if check == func_a:
        result = a
        to_append = func_a
    elif check == func_b:
        result = b
        to_append = func_b
    elif check == func_d:
        to_append = func_d        
        result = d
     
    #output_box.append(to_append)
    #np.unique(output_box)
    #output_box.sort()
    

print("x1 = %.16f" % result[0])
print("x2 = %.16f" % result[1])
print("f(x1, x2) = %.16f" % function(result)) # maksimum
#print("Closest result: ", output_box[0],"\n")
#print(output_box,"\n")




    
