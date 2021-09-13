from matrix import *

print(f'\nGauss-Jordan Elimination method')

for i in range(n):
    
    try:  
        for j in range(n):
            
            if i != j:
                fator = matrix[j][i]/matrix[i][i]

                for k in range(n+1):
                    matrix[j][k] -= fator * matrix[i][k]
            
    except ZeroDivisionError:
        print('There is no real solution, zero division detected.')
        break
    
    if show == str('Y'):
        np.set_printoptions(suppress=True)
        print(f'\nScaling step {i+1}ᵒ: \n{matrix}')

    else:
        continue

vector_two = np.zeros(n)

for i in range(n):
    vector_two[i] = round(matrix[i][n]/matrix[i][i], 3)*parameter

    for j in range(n):

        if i == j:
            matrix[i][j] = round(matrix[i][n]/matrix[i][i], 3)*parameter
            matrix[i][n] = round(matrix[i][n]/matrix[i][n], 3)*parameter
        else:
            continue

print(f'\nLast scaling step: \n{matrix}')


if method == str('b'):
    
    print('\nSolution for the coefficients: ')

    for i in range(n):
        print(f'a{i+1} = {vector_two[i]}', end = '\t')



