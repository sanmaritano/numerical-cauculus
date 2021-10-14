from math import sqrt
import subprocess
import sys

try:
    from scipy import integrate
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'scipy'])
finally:
    from scipy import integrate


class IntegralMethod:

    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def exact_solution(self):
        return integrate.quad(f, self.a, self.b)

    def __str__(self):
        return f'{self.a}'

class TrapezoidMethod(IntegralMethod):

    def trapezoid(self):
        h = (self.b-self.a)/float(self.n)
        s = 0.5*(f(self.a) + f(self.b))

        for i in range(1, self.n):
            s += f(self.a + i*h)

        return h*s

class SimpsonMethod(IntegralMethod):

    def simpson_third(self):
        h = (self.b-self.a)/float(self.n)
        s = (f(self.a) + f(self.b))

        for i in range(1, self.n): 
            k = self.a + i*h
            mod = i/2
            
            if mod == 1%2:
                s += 2*f(k)
            else:
                s += 4*f(k)
        
        s *= h/3

        return s
        
    def simpson_second(self):

        h = (self.b-self.a)/float(self.n)
        s = (f(self.a) + f(self.b))

        for i in range(1, self.n):
            mod = i/8
            
            if mod == 1%3:
                s += 2*f(self.a + i*h)
            else:
                s += 3*f(self.a + i*h)
        
        s *= (3*h)/8

        return s

class GaussMethod(IntegralMethod):
    def gauss_quad(self):
    
        x1 = -sqrt(3)/3
        x2 = sqrt(3)/3

        #Parametrizacao: 
        
        t1 = ((self.b - self.a)*x1 + (self.a + self.b))/2
        t2 = ((self.b - self.a)*x2 + (self.a + self.b))/2

        dt = (self.b - self.a)/2
        
        integral = (f(t1) + f(t2))*dt

        return integral

def f(x):
    return 1/x







