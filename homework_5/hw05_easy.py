# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
list_g = [1, 2, 4, 0]
new_cool_lst = [el**2 for el in list_g]

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

l1 = ['Яблоко', 'Апельсин', 'Груша']
l2 = ['Арбуз','Кокос','Апельсин','Дыня','Груша','Киви']
res = set([x for x in l1 + l2 if x in l1 and x  in l2])
print(res)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

l3 = [2,4,-10,15,13,21]
res = [x for x in l3 if x % 3 == 0 and x > 0 and x % 4 != 0 ]
print(res)
