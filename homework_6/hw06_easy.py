# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5


a = float(input("a = "))
b = float(input("b = "))
c = avg(a, b)
print("Среднее геометрическое = {:.2f}".format(c))
==========================================================================================================
def avg(a, b):
    """Вернуть среднее геометрическое чисел 'a' и 'b'.

    Параметры:
        - a, b (int или float).

    Результат:
        - float.
    """
    return (a * b) ** 0.5
try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except ValueError as valerr:
    print("\033[35m {}".format('Ошибочка, вводите числовые значения'))
except Exception as ex:
    print('Произошло неведомое {0}'.format(ex))

os.mkdir(path, mode=0o777, *, dir_fd=None)



# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

dir_name = 'testdir'
for i in range(1,11):
    c = dir_name + str(i)
    os.mkdir(c, mode=0o777, dir_fd=None)

for i in range(1,11):
    curdir = os.getcwd() + '\\' + dir_name + str(i)
    os.removedirs(curdir)


# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.

import os
i = None
d = os.listdir(os.getcwd())
directory = os.getcwd()
print(d)
print('Список папок в текущей директории:')
for i in d:
    tmp_var = directory = os.getcwd() + '\\' + str(i)
    if os.path.isdir(tmp_var):
        print(i, end=' ')

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
import shutil

z = os.path.basename(__file__)
v = z.split('.')

new_file_path= os.getcwd() + '\\' +  v[0] + '_copy.' + v[1]

p = os.path.abspath(z)
n = os.path.abspath(new_file_path)

shutil.copyfile(p, n)