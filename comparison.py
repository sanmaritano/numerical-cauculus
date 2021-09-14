from integral_methods import *

def f(x):
    #type your equation bellow.
    return 1/x

a = float(input("Type your first integral coefficient: "))
b = float(input("Type your second integral coefficient: "))
n = int(input("Type your integral subintervals: "))

exact = integrate.quad(f, a, b)

result_trap = trapezoid(f, a, b, n=1)
result_trap_rep = trapezoid(f, a, b, n)

result_s13 = simpson_third(f, a, b, n=1)
result_s38 = simpson_second(f, a, b, n=1)
result_s13_rep = simpson_third(f, a, b, n)
result_s38_rep = simpson_second(f, a, b, n)
result_gauss = gauss_quad(f, a, b)

erro_trap = erro(exact[0], result_trap)
erro_trap_rep = erro(exact[0], result_trap_rep)
erro_s13 = erro(exact[0], result_s13)
erro_s38 = erro(exact[0], result_s38)
erro_s13_rep = erro(exact[0], result_s13_rep)
erro_s38_rep = erro(exact[0], result_s38_rep)
erro_gauss = erro(exact[0], result_gauss)

print(f'\nThe exact integral solution is: {exact[0]:.4f}.')

print()
print(f'\nCOMPARISON BETWEEN TRAPEZOIDAL RULE WITOUTH AND WITH SUBINTERVALS.')
print(f'\nMétodo do Trapézio = {result_trap:.4f} \
    Erro = {erro_trap:.2f}% \
    Método do Trapézio Repetido = {result_trap_rep:.4f}\
    Erro = {erro_trap_rep:.2f}% \
    ', end='\t')

print()
print()
print(f'\nCOMPARISON WITH SIMPSON 1/3 AND 3/8 METHODS (without subintervals).')
print(f'\nMétodo Simpson 1/3 = {result_s13:.4f} \
    Erro = {erro_s13:.2f}% \
    Método Simpson 3/8 = {result_s38:.4f}\
    Erro = {erro_s38:.2f}% \
    ', end='\t')

print()
print()
print(f'\nCOMPARISON WITH SIMPSON 1/3 AND 3/8 METHODS (with subintervals).')
print(f'\nMétodo Simpson 1/3 = {result_s13_rep:.4f} \
    Erro = {erro_s13_rep:.2f}% \
    Método Simpson 3/8 = {result_s38_rep:.4f}\
    Erro = {erro_s38_rep:.2f}% \
    ', end='\t')

print()
print()
print(f'\nGAUSSIAN QUADRATURE RULE SOLUTION.')
print(f'\nQuadratura Gaussiana = {result_gauss:.4f}\
    Erro = {erro_gauss:.2f}%', end='\t')

