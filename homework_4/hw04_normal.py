# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
def fibonacci(n, m):
        def fib_elem_val(x):
            fib_t1 = fib_t2 = 1
            x -= 2
            while x > 0:
                fib_t1, fib_t2 = fib_t2, fib_t1 + fib_t2
                x -= 1
            return fib_t2
        if m == n:
            print(fib_elem_val(n))
        else:
            fib2=fib_elem_val(m)
            fib1=fib_elem_val(n)
            fib2r = fib1 + fib_elem_val(n - 1)
            print(fib1,end=' ')
            print(fib2r,end=' ')
            i = 0
            while i < ((m-n)-1):
                fib_sum = fib1 + fib2r
                fib1 = fib2r
                fib2r = fib_sum
                i = i + 1
                print(fib_sum,end=' ')

n = int(input("Номер первого элемента ряда Фибоначчи: "))
m = int(input("Номер последнего элемента ряда Фибоначчи: "))
if n == m:
    print('Значение эелемента в ряду Фибонначи: ')
    fibonacci(n, m)
elif n == 1 and m == 2:
    print('Ряд Фибонначи для заданных элементов: 1 1')
elif n == 1 and m == 1:
    print('Ряд Фибонначи для заданных элементов: 1')
elif n == 1:
    print('Ряд Фибонначи для заданных элементов:')
    print('1',end=' ')
    fibonacci(n+1, m)
else:
    print('Ряд Фибонначи для заданных элементов: ')
    fibonacci(n, m)



# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp

a = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]
print('Initial list: ',a)
sort_to_max(a)
print('Sorted List: ',a)



# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

Нет идей


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def side_len(a,b):
    len_side=((((b[0] - a[0])**2) + ((b[1] - a[1])**2))**0.5 )
    return len_side

def cut_x(x):
    s= input('Введите Kooрдинаты отрезка через \",\": ')
    x = s.split(',')
    for i in range(len(x)):
        x[i] = float(x[i])
    return x
#
a = []
b = []
c = []
d = []

a=cut_x(a)
b=cut_x(b)
c=cut_x(c)
d=cut_x(d)

ab_len=side_len(a,b)
dc_len=side_len(d,c)
ad_len=side_len(a,d)
bc_len=side_len(b,c)

if ab_len == dc_len and bc_len==ad_len:
    print('Storony yavlyautsya vershinami')
else:
    print('Storony NE yavlyautsya vershinami')









