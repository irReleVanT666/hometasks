
__author__ = 'Селиверстов Ю.В'

# Задача-1: Ввести ваше имя и возраст в отдельные переменные,
# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.

# TODO: код пишем тут...

print ('What is Your name, mortal?')
name = input()
print ('How old are You,', name,'?')
age = int(input ())
agediff = age - 18

if agediff in [1,21,31,41,51,61,71,81,91,101] :
    print (name,',starshe 18 na',agediff,'god')
elif agediff in [2,3,4,22,23,24,32,33,34,42,42,44,52,53,54,62,63,64,72,73,74]:
    print (name,',starshe 18 na',agediff,'goda')
elif agediff > 0:
    print (name,',starshe 18 na',agediff,'let')
elif agediff in [-1,-21,-31,-41,-51,-61,-71,-81,-91,-101] :
    print (name,',mologe 18 na',abs(agediff),'god')
elif agediff in [-2,-3,-4,-22,-23,-24,-32,-33,-34,-42,-42,-44,-52,-53,-54,-62,-63,-64,-72,-73,-74]:
    print (name,',mologe 18 na',abs(agediff),'goda')
else:
    print (name,',mologe 18 na',abs(agediff),'let')


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

# TODO: код пишем тут...
print ('enter the X')
varX = input()
print ('enter the Y')
varY = input()


varC = varX
varX = varY
varY = varC
print ('Ha ha ha , X =',varX,'and Y =',varY)


# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

# TODO: код пишем тут...
import math

print ('Enter the A')
varA = int(input ())
print ('Enter the B')
varB= int(input ())
print ('Enter the C')
varC = int(input ())

varD = varB**2 - 4*varA*varC
print ('----------------------------------------')
print('Diskriminant = ',varD)

if varD == 0:
    varX = ( varB*-1 + math.sqrt(varB**2 - 4*varA*varC)) / (2*varA)
    print ('X1=X2 = ',varX)
elif varD < 0:
    print ('----------------------------------------')
    print ('Korni kompleksnye 4isla')
elif varD > 0:
    varX = ( varB*-1 + math.sqrt(varB**2 - 4*varA*varC)) / (2*varA)
    varNegX = ( varB*-1 - math.sqrt(varB**2 - 4*varA*varC)) / (2*varA)
    print ('----------------------------------------')
    print ('Koren X1 =',varX,' | ','Koren X2 =',varNegX)
    print ('----------------------------------------')

             

