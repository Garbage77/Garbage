import math
def F(x):
    c=x.replace('.','',1).replace('-','',1)
    while not( x.isnumeric() or x.count('-')==1 and x[0]=='-' and x.replace('-','').isnumeric() or\
         x[0]!='.' and x.replace('.','',1).isnumeric() and x[-1]!='.' or\
         x.count('-')==1 and x[0]=='-' and x[0]!='.' and x[-1]!='.' and c.isnumeric()):
        print('введенный символ не является числом, введите число:')
        x=input()
        c=x.replace('.','',1).replace('-','',1)
    return x
print('Калькулятор')
g='1'
while g=='1':
    print('Введите необходимую функцию:\nСложение - 1\nВычитание - 2\nУмножение - 3\nДеление - 4\nСтепень - 5\nЛогарифм - 6\nОкругление в большую сторону до N знака после запятой - 7\nОкругление в меньшую сторону до N знака после запятой - 8')
    fun=input()
    if fun in '1234':
        a = input('Введите первое число:')
        a = float(F(a))
        b = input('Введите второе число:')
        b = float(F(b))

    if fun=='1':
        print('Сумма чисел = ',a+b)

    if fun=='2':
        print('Разность чисел = ',a-b)

    if fun=='3':
        print('Произведение чисел = ',a*b)

    if fun=='4':
        if b==0:
            print ('На ноль делить нельзя')
        else:
            print('Частное чисел = ',a/b)

    if fun=='5':
        a = input('Введите число:')
        a = float(F(a))
        b = input('Введите показатель степени:')
        b = float(F(b))

    if fun=='6':
        a = input('Введите основание логарифма:')
        a = float(F(a))
        while a==1 or a<=0:
            a = input('Введите другое значения основания логарифма, это не подходит по ОДЗ:')
            a = float(F(a))
        b = input('Введите аргумент логарифма:')
        b = float(F(b))
        while b<=0:
            b = input('Введите другой аргумент, этот не подходит:')
            b = float(F(b))
        print('Ответ = ',math.log(b,a))

    if fun=='5':
        print('Ответ = ',a**b)

    if fun=='7':
        a=input('Введите число:')
        a=float(F(a))
        n=input('Введите до какого числа нужно округлить:')
        while not (n.isnumeric()):
            n=input('Округлить можно только до целых чисел после запятой, введите другое:')
        n=int(n)
        index = str(a).index('.')
        z=str(a)[index+1:]
        if z.count('1') + z.count('2') + z.count('3') + z.count('4') + z.count('5') + z.count('6') + z.count('7') + z.count('8') + z.count('9') + z.count('0')>n:
            b=str(a)[index+n+1]
            if b!=0:
                a=float(str(a)[:(index+n+1)])+0.1**n
                print('Ваше число = ',a )
            else:
                print('Ваше число = ',str(a)[:(index+n+1)])
        else:
            print('Ваше число = ',str(a)[:(index+n+1)])
        
    if fun=='8':
        a=input('Введите число:')
        a=float(F(a))
        n=input('Введите до какого числа нужно округлить:')
        while not (n.isnumeric()):
            n=input('Округлить можно только до целых чисел после запятой, введите другое:')
        n=int(n)
        index=str(a).find('.')
        a=str(a)[:(index+n+1)]
        print(a)
    g=input('Хотите запустить программу ещё раз?\n1 - да\nлюбая другая клавиша - выход из программы\n')
    

    
    
