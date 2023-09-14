#if
print('команда if')
a = int(input('введите число:'))
if a>5:
    print('больше 5')
elif a<=5:
    print('меньше 5')
#else
print('команда else')
a =input('введите слово:')
if len(a)>5:
    print('больше 5 букв')
else:
    print('меньше 5 букв')
#input
print('команда input')
a = input()
print(a)
#while
print('команда while')
m = 'ggg'
i = 0
print('m = ',m)
while i<3:
    m=m+'r'
    i+=1
print('m = ',m)
#for
print('команда for')
mas = []
a = 23
print('mas = ',mas)
for i in range(0,2):
    mas.append(a)
print('mas = ',mas)
