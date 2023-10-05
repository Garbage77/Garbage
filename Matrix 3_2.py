import numpy as np 
import time 
m=[0] * 3
for i in range (3):
    m[i] = [0] * 3

print('Введите данные матрицы по одному элементу за раз')
for i in range(3):
     for j in range(3):
        print('Введите элемент', i+1, 'строки', j+1, 'столбца:')
        m[i][j]=float(input())
        
start_time = time.time()
for i in range(0, 1000000):
    pass
b = np.linalg.inv(m)

print ("Матрица A:\n", m)
print ("Обратная матрица к A:\n", b)
end_time = time.time()
elapsed_time = end_time - start_time
print('Elapsed time: ', elapsed_time)
