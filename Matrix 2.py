import numpy as np
g = 1
n = 0
p = 0
while g == 1:
    c=int(input("Выберите функцию:\n1 - Транспонирование матрицы\n2 - умножение двух матриц\n3 - определение ранга матрицы\n4 - Выход из программы\n"))
    if c==1:
        n = int(input("Введите количество строк:\n"))
        p = int(input("Введите количество столбцов:\n"))
        a = np.zeros((n,p),'int')
        for i in range(0,n):
            for j in range(0,p):
                print("Введите элемент a[",i+1,":",j+1,"]:")
                a[i,j] = float(input())
        print("Ваша матрица:")
        print(a)
        print("Транспонированная матрица:")
        print(a.transpose())
    if c == 2:
        n = int(input("Введите количество строк:\n"))
        p = int(input("Введите количество столбцов:\n"))
        a = np.zeros((n,p),'int')
        for i in range(0,n):
            for j in range(0,p):
                print("Введите элемент a[",i+1,":",j+1,"]:")
                a[i,j] = float(input())
        n = int(input("Введите количество строк 2-ой матрицы:\n"))
        p = int(input("Введите количество столбцов 2-ой матрицы:\n"))
        a2 = np.zeros((n,p),'int')
        for i in range(0,n):
            for j in range(0,p):
                print("Введите элемент a[",i+1,":",j+1,"]:")
                a2[i,j] = float(input())
        print("произведение матриц равно:\n",np.dot(a,a2))
    if c==3:
        n = int(input("Введите количество строк:\n"))
        p = int(input("Введите количество столбцов:\n"))
        a = np.zeros((n,p),'int')
        for i in range(0,n):
            for j in range(0,p):
                print("Введите элемент a[",i+1,":",j+1,"]:")
                a[i,j] = float(input())
        print("ранг матрицы равен:\n",np.linalg.matrix_rank(a))
    if c == 4:
        g = 2
        print("Спасибо что используете нашу программу, пока.\n")