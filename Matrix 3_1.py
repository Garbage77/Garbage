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
#Создание матрицы -1
det_A = (m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1]) - (m[0][2] * m[1][1] * m[2][0] + m[0][0] * m[2][1] * m[1][2] + m[2][2] * m[1][0] * m[0][1])
if det_A == 0:
    print("У этой матрицы нет обратной матрицы")
    exit()

opr=[0] * 3
for i in range (3):
    opr[i] = [0] * 3
    
opr[0][0] = m[1][1]*m[2][2]-m[1][2]*m[2][1]
opr[0][1] = m[1][0]*m[2][2]-m[1][2]*m[2][0]
opr[0][2] = m[1][0]*m[2][1]-m[1][1]*m[2][0]
opr[1][0] = m[0][1]*m[2][2]-m[2][1]*m[0][2]
opr[1][1] = m[0][0]*m[2][2]-m[2][0]*m[0][2]
opr[1][2] = m[0][0]*m[2][1]-m[2][0]*m[0][1]
opr[2][0] = m[0][1]*m[1][2]-m[1][1]*m[0][2]
opr[2][1] = m[0][0]*m[1][2]-m[1][0]*m[0][2]
opr[2][2] = m[0][0]*m[1][1]-m[1][0]*m[0][1]

for i in range (3):
    for j in range (3):
        opr[i][j]=opr[i][j]*((-1)**(i+j+2))

Topr=[[0]* 3 for _ in range (3)]
for i in range (3):
    for j in range (3):
        Topr[j][i]=opr[i][j]
        
for i in range (3):
    for j in range (3):
        opr[i][j]=Topr[i][j]/det_A

print("Ваша матрица")
for row in m:
    print(row)

print("Матрица обратная ей")
for row in opr:
    print(row)
end_time = time.time()
elapsed_time = end_time - start_time
print('Elapsed time: ', elapsed_time)

        
    

