from matrix import *

print(f'\nGauss Elimination method')

for i in range(n):
    
    try:  
        for j in range(i+1, n):
            fator = matrix[j][i]/matrix[i][i]

            for k in range(n+1):
                matrix[j][k] -= fator*matrix[i][k]

    except ZeroDivisionError:
        print('There is no real solution, zero division detected.')
        break

    if  show == str('Y'):
            np.set_printoptions(suppress=True)
            print(f'\nScaling step {i+1}ᵒ: \n{matrix}')

    else:
        continue


vector_one = np.zeros(n)

vector_one[n-1] = matrix[n-1][n]/matrix[n-1][n-1]

for i in range(n-2, -1, -1):
    vector_one[i] = matrix[i][n]

    for j in range(i+1, n):
        vector_one[i] -= matrix[i][j]*vector_one[j]

    vector_one[i] = round(vector_one[i]/matrix[i][i], 3)
    
if method == str('a'):

    print('\nWe find the solution solving the linear system')

    print('\nSolution for the coefficients:: ')
    for i in range(n):

        print(f'a{i+1} = {vector_one[i]*parameter}', end = '\t')
