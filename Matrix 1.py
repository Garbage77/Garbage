def F(x):
    while True:
        try:
            x = int(x)
            return x
        except ValueError:
            print("То что вы ввели не является подходящим элементом.\n")
            x = input("Введите другое число, которое подходит по условиям: ")

def razm(razm):
    while int(razm)!=1 and int(razm)!=2 and int(razm)!=3:
        razm = F(input("Введите другое значение, варианта который вы ввели не существует\n"))
    else:
        return razm

def razm2(razm):
    while int(razm)!=2 and int(razm)!=3:
        razm = F(input("Введите другое значение, варианта который вы ввели не существует\n"))
    else:
        return razm

def Fl(x):
    while True:
        try:
            x = float(x)
            return x
        except ValueError:
            print("То что вы ввели не является подходящим элементом.\n")
            x = input("Пожалуйста введите число: ")

def Vi(razm):
    while not(razm in '1') and not(razm in '2') and not(razm in '3') and not(razm in '4') :
        razm = input("Введите другое значение, варианта который вы ввели не существует\n")
    else:
        return razm
    
g = 1

while g == 1:
    c=Vi(input("Выберите функцию:\n1 - Транспонирование матрицы\n2 - умножение двух матриц\n3 - определение ранга матрицы\n4 - Выход из программы\n"))
    if c == '1' or c == '2':
        razmSto = razm(F(input("Выберите размерность матрицы\nКол-во строк:\n(От 1 до 3)\n")))
        razmStr = razm(F(input("Кол-во столбов:\n(От 1 до 3)\n")))      

        massiv=[0] * razmSto
        for i in range (razmSto):
            massiv[i] = [0] * razmStr

        print("Введите данные в массив, по одному элементу за раз: ")
        for i in range(razmSto):
            for j in range(razmStr):
                print('Введите элемент', i+1, 'строки', j+1, 'столбца:')
                massiv[i][j]=Fl(input())

#Транспонирование матрицы
        if c == '1':

            Tmassiv = [[0]*razmSto for _ in range (razmStr)]
            for i in range(razmSto):
                for j in range(razmStr):
                    Tmassiv[j][i] = massiv[i][j]
        
            print("Оригинальная матрица:")
            for row in massiv:
                print(row)

            print("Транспонированная матрица:")
            for row in Tmassiv:
                print(row)

#Умножение матриц    
        if c == '2':
            
            print("Создайте вторую матрицу: ")
            razmSto2 = razm(F(input("Выберите размерность матрицы\nКол-во строк:\n(От 1 до 3)\n")))
            razmStr2 = razm(F(input("Кол-во столбов:\n(От 1 до 3)\n")))

            if not(razmSto == razmStr2):
                print("Матрицы умножить нельзя")
                continue

            massiv2=[0] * razmSto2
            for i in range (razmSto2):
                massiv2[i] = [0] * razmStr2

            print("Введите данные в массив, по одному элементу за раз: ")
            for i in range(razmSto2):
                for j in range(razmStr2):
                    print('Введите элемент', i+1, 'строки', j+1, 'столбца:')
                    massiv2[i][j]=Fl(input())

            massivresult=[[0] * razmStr for _ in range (razmSto2)]
            for i in range (razmStr):
                for j in range (razmSto2):
                    for k in range (razmStr2):
                        massivresult[i][j]+=massiv[k][i]*massiv2[j][k]
            print("Первая матрица:")
            for row in massiv:
                print(row)

            print("Вторая матрица:")
            for row in massiv2:
                print(row)

            print("Их произведение:")
            for row in massivresult:
                print(row)

    if c == '3':
        razmer = razm(F(input("Выберите размерность матрицы (2 или 3)\n")))

        m=[0] * razmer
        for i in range (razmer):
            m[i] = [0] * razmer

        print("Введите данные в массив, по одному элементу за раз: ")
        for i in range(razmer):
            for j in range(razmer):
                print('Введите элемент', i+1, 'строки', j+1, 'столбца:')
                m[i][j]=Fl(input())
            
        mas = []
            
        if razmer == 3:
            if ((m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1]) - (m[0][2] * m[1][1] * m[2][0] + m[0][0] * m[2][1] * m[1][2] + m[2][2] * m[1][0] * m[0][1]))!=0:
                print("Ранг матрицы = 3")
                continue
            for i in range (razmer-1):
                for j in range (razmer-1):
                    mas.append(m[i][j]*m[i+1][j+1]-m[i][j+1]*m[i+1][j])
            if mas.count(0)!=len(mas):
                print("Ранг матрицы = 2")
                continue
            if m[0].count(0) == 3 and m[1].count(0) == 3 and m[2].count(0) == 3:
                print("Ранг матрицы = 0")
                continue
            else:
                print("Ранг матрицы = 1")

        if razmer == 2:
            if m[0][0]*m[1][1]-m[0][1]*m[1][0]:
                print("Ранг матрицы = 2")
                continue
            if m[0].count(0) == 3 and m[1].count(0) == 3:
                print("Ранг матрицы = 0")
                continue
            else:
                print("Ранг матрицы = 1")
                continue
            
    if c == '4':
        g = 2
        print("Спасибо что используете нашу программу, пока.\n")
    

























    
