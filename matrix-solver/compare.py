from matrix import *
from gauss_elimination import vector_one
from gauss_jordan import vector_two

if method == str('c'):

    print()
    print('-'*100)
    print('\nSolution using Gauss Elimination: ')

    for i in range(n):
        print(f'd{i+1} = {vector_one[i]}', end = '\t')

    print()
    print('-'*100)
    print('\nSolution using Gauss-Jordan Elimination: ')

    for i in range(n):
        print(f'd{i+1} = {vector_two[i]}', end = '\t')




