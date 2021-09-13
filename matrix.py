from back_code import *

print(f'\na)Gauss Elimination method.')
print(f'\nb)Gauss-Jordan Elimination method.')
print(f'\nc)Compare methods.')

method = str(input('What method do you wish to use?: '))    
show = str(input('Do you wish to print the matrix scaling? (Y/N): '))

n = int(input('Input the square matrix size: '))

parameter = float(input('Input any multiplier parameter, if you want: '))

print('\nPosterily, insert augmented matrix coefficients: ')

print()

matrix = np.zeros((n, n+1))

for i in range(n):
    for j in range(n+1):
        matrix[i][j] = float(input(f'Input coefficient M({i+1}x{j+1}): '))

print(f'\nAugmented matrix: \n{matrix}')

print()