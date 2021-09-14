from math import sqrt
import subprocess
import sys

try:
    from scipy import integrate
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'scipy'])
finally:
    from scipy import integrate


def erro(exact, obtained):
    d = abs(exact-obtained)
    return (d/exact)*100

def trapezoid(f, a, b, n):
    
    h = (b-a)/float(n)
    s = 0.5*(f(a) + f(b))

    for i in range(1, n):
        s += f(a + i*h)

    return h*s

def simpson_third(f, a, b, n):
    
    h = (b-a)/n
    s = (f(a) + f(b))

    for i in range(1, n): 
        k = a + i*h
        mod = i/2
        
        if mod == 1%2:
            s += 2*f(k)
        else:
            s += 4*f(k)
    
    s *= h/3

    return s

def simpson_second(f, a, b, n):
    
    h = (b-a)/n
    s = (f(a) + f(b))

    for i in range(1, n):
        mod = i/8
        
        if mod == 1%3:
            s += 2*f(a + i*h)
        else:
            s += 3*f(a + i*h)
    
    s *= (3*h)/8

    return s

def gauss_quad(f, a, b):
    
    x1 = -sqrt(3)/3
    x2 = sqrt(3)/3

    #Parametrizacao: 
    
    t1 = ((b - a)*x1 + (a + b))/2
    t2 = ((b - a)*x2 + (a + b))/2

    dt = (b - a)/2
    
    integral = (f(t1) + f(t2))*dt

    return integral
