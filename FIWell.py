import numpy as np
import matplotlib.pyplot as plt


max_iter = 10 #this fixes errent zeros

def find_sign_changes(f, step, a, b):
    x = a
    pairs = []
    while (x + step < b):
        if (f(x + step)/f(x) < 0):
            pairs.append([x, x+step])
        x += step
    return pairs

def bisection(f, pairs, tolerance, max_iter):
    zeroes = []
    for pair in pairs:
        midpoint = (pair[1] - pair[0])/2 + pair[0]
        iter = 1
        while (abs(f(midpoint)) > tolerance and iter < max_iter):
            if (f(midpoint)/f(pair[0]) < 0):
                pair[1] = midpoint
            else:
                pair[0] = midpoint
            midpoint = (pair[1] - pair[0])/2 + pair[0]
            iter += 1
        if (iter < max_iter):
            zeroes.append(midpoint)
    return zeroes
#V_0 = 4E-17
#V_0 =8E-17
V_0 = 8E-15 #Joules
a = 1E-10 #meters
h_bar = 1.054E-34 #J*s
m_e = 9.109E-31 #Kg

# Equations

z_0 = (a/h_bar)*np.sqrt(2*m_e*V_0)

# Calculation

z = np.linspace(0, z_0, 1000)

def z_1(z):
    if (z == 0):
        return 1
    else:
        return np.sqrt((z_0/z)**2 - 1) - np.tan(z)

def z_2(z):
    if (z == 0):
        return 1
    else:
        return np.sqrt((z_0/z)**2 - 1) + 1/np.tan(z)

pairs =find_sign_changes(z_1, 0.1, 0, 15)
zeros =bisection(z_1, pairs, 1E-10, 1000)

pairs_2 = find_sign_changes(z_2, 0.1, 0, 15)
zeros_2 = bisection(z_2, pairs_2, 1E-10, 1000)

print(zeros,zeros_2)

E = []
n = 0

for z in zeros:
    E.append(h_bar**2/(2*m_e*a**2)*z**2 - V_0)

for z in zeros_2:
    E.append(h_bar**2/(2*m_e*a**2)*z**2 - V_0)
#converting the discrete case into more of an infinite one.
print(E)
# 
def Infinite(n):
    return (n*np.pi*h_bar)**2/(8*m_e*a**2) - V_0

print("infinite", Infinite(1), Infinite(2), Infinite(3), Infinite(4), Infinite(5),Infinite(6), Infinite(7), Infinite(8))

x = np.linspace(-15,15,5)
plt.plot(x, E)
#plt.plot(x, (Infinite(1), Infinite(2), Infinite(3), Infinite(4), Infinite(5)))
plt.plot(x, x)
#plt.ylim(-8.3E-15, -7.6E-15)
plt.show()