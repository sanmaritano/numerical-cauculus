import sys
from integral_methods import IntegralMethod, TrapezoidMethod, SimpsonMethod, GaussMethod
from errors import NumericalErrors

def f(x):
    #type your equation bellow.
    return 1/x

a = float(input("Type your first integral coefficient: "))
b = float(input("Type your second integral coefficient: "))
n = int(input("Type your integral subintervals: "))


ref = IntegralMethod(a, b, n)
trap = TrapezoidMethod(a, b, n)
simp = SimpsonMethod(a, b, n)
gauss = GaussMethod(a, b, n)

scipy_solution = ref.exact_solution()
solution = (scipy_solution[0])


result_trap = trap.trapezoid()
result_s13 = simp.simpson_third()
result_s38 = simp.simpson_second()
result_gauss = gauss.gauss_quad()

e = NumericalErrors(solution, result_trap)
e2 = NumericalErrors(solution, result_s13)
e3 = NumericalErrors(solution, result_s38)
e4 = NumericalErrors(solution, result_gauss)

erro_t = e.relative_error()
erro_s13 = e2.relative_error()
erro_s38 = e3.relative_error()
erro_g = e4.relative_error()


print(f'\nThe exact integral solution is: {solution:.4f}.')

print()
print(f'\nCOMPARISON BETWEEN TRAPEZOIDAL, SIMPSON 1/3 AND 3/8 METHODS.')
print(f'\nTrapezoid Result = {result_trap:.4f}\
    \nTrapezoid Relative Error = {erro_t:.2f}%')

print()

print(f'\nSimpson 1/3 Result = {result_s13:.4f}\
    \nSimpson 1/3 Relative Error = {erro_s13:.2f}%\
    \nSimpson 3/8 Result = {result_s38:.4f}\
    \nSimpson 3/8 Relative Error = {erro_s38:.2f}%')

print()

print(f'\nGAUSSIAN QUADRATURE RULE SOLUTION.')
print(f'\nGaussian Quadrature = {result_gauss:.4f}\
    \nTrapezoid Relative Error = {erro_g:.2f}%')

