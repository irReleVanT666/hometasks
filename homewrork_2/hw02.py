
__author__ = 'Ваши Ф.И.О.'

# Задача-1: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользоваться данным ресурсом можно только с 18 лет"

print ('How old are U?')
varAge = int(input())
if varAge >= 18 :
	print('Access granted')
else:
	print ('You are too Young to use this resourse') 

# Задача-2: Напишите программу, которая спрашивает "Четные или нечетные?", в зависимости от ответа,
# используя цикл с предусловием while или for in
# вывести в одну строку через пробел соотвествующие числа от 0 до 20
# Пример работы:
# $ "Четные или нечетные?"
# четные
# 0 2 4 6 8 10 12 14 16 18 20
# $ "Четные или нечетные?"
# нечетные
# 1 3 5 7 9 11 13 15 17 19
# $ "Четные или нечетные?"
# qwerty (или любая другая строка)
# Я не понимаю, что вы от меня хотите...

print ('4etnie ili ne4etnie?')
varAnsw = input()
i = 0
if varAnsw == 'ne4etnie?':
	for i in range(1,20,2):
		print(i, end=',')
if varAnsw == '4etnie':
	for i in range(0,20,2):
		print(i, end=',')
else:
	print('Can't get what do you mean...')		
	


# Задача-3: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

print('Please, enter a nubmer:')
inpVar = input()
strVar = str(inpVar)
lstVar = list(map(int, strVar))
maxVar = max(lstVar)
print('The biggest number is', maxVar)

#честно стырил с интернета. понимания как с for решить что то нет(