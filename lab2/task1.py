import json
import numpy as np

matrix = np.load('lab2/files/first_task.npy')
size = matrix.size

matrix_props = {
    'sum': 0,
    'avg': 0,
    'sumMD': 0,
    'avgMD': 0,
    'sumSD': 0,
    'avgSD': 0,
    'max': 0,
    'min': 0
}

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
       
        item = matrix[i][j]
        
        matrix_props['sum'] += item
       
        if i == j:
            matrix_props['sumMD'] += item

        if j == matrix.shape[1] - i - 1:
            matrix_props['sumSD'] += item

        if matrix_props['max'] < item:
            matrix_props['max'] = item

        if matrix_props['min'] > item:
            matrix_props['min'] = item

matrix_props['avg'] = matrix_props['sum'] / size
matrix_props['avgMD'] = matrix_props['sumMD'] / matrix.shape[0]
matrix_props['avgSD'] = matrix_props['sumSD'] / matrix.shape[0]

for key in matrix_props.keys():
    matrix_props[key] = float(matrix_props[key])

with open ('lab2/files/results/task1_1.json', 'w', encoding = 'utf-8') as file:
    json.dump(matrix_props, file, indent=1)

norm_matrix = matrix / matrix_props['sum']
np.save('lab2/files/results/task1_2.npy', norm_matrix)
