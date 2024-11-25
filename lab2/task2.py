import numpy as np
import os

matrix = np.load('/root/lab2/files/second_task.npy')

x = []
y = []
z = []

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i][j] > 549:
            x.append(i)
            y.append(j)
            z.append(matrix[i][j])

np.savez('/root/lab2/files/results/task2_1.npz', x=x, y=y, z=z)
np.savez_compressed('/root/lab2/files/results/task2_2.npz', x=x, y=y, z=z)

size1 = os.path.getsize('/root/lab2/files/results/task2_1.npz')
size2 = os.path.getsize('/root/lab2/files/results/task2_2.npz')

print(f'savez = {size1}')
print(f'savez_compressed = {size2}')
print(f'diff = {size1 - size2}')