#комприкейшен:
# import random
# my_list = [random.randint(0,1000) for _ in range(10)]
# print(my_list)

# map: функция которая заставляет другую функцию применится к каждому элементу списка
# string = '123 584 54 6887 889 5 88 79878 99'
# my_list = string.split()
# print(my_list)

# def summa(a):
#     return int(a) + 10

# my_list = list(map(summa, my_list)) # перед мап всегда нужно указывать коллекцию: список list, строка string или множества set, кортеж tuple, функция может быть своя как в примере или любая из библиотеки: int,  и тд. 
# print(my_list)
# #    ИЛИ
# my_list = list(map(int, my_list)) # переведет строку и интеджер

#FILTER
# string = '123 584 54 6887 889 5 88 79878 99'
# my_list = string.split()
# print(my_list)

# def func(x : int):
#     if x % 2 != 0:
#         return x
# my_list = list(map(int, my_list)) #преобразуем в инт
# my_list = list(filter(func, my_list))
# print(my_list)

# #  LAMBDA
# my_list = list(filter(lambda x : x % 2 != 0, my_list)) #прописываем условие в строку вместо всей функции

# # ENUMERATE пронумеровывает с нуля, совподает с номером индекса
# string = '123 584 54 6887 889 5 88 79878 99'
# my_list = string.split()

# for i, k in enumerate(my_list, 1): # i - индекс, к - значение, 1 - с какого номера начинать нумеровать, если нужно вывести список учеников например, можно ставить любое число вместо еденицы
#   print(i, k)

# # ZIP
# string = '123 584 54 6887 889 5 88 79878 99'
# numbers = [555,55654,45897,255,366,84,326,88,5]
# my_list = string.split()
# print(my_list)
# print(numbers)
# new_list = list(zip(my_list, numbers)) # складывает в кортежи значения из разных списков , коли-во элементов должно быть одинаково иначе соединит только сколько будет итераций и дальше не пойдет(если в одном будет 5 в другом 3 элемента, сработает только 3 элемпнта и прекратит работу)
# print(new_list)

# #можно сделать словарь:
# string = '123 584 54 6887 889 5 88 79878 99'
# numbers = [555,55654,45897,255,366,84,326,88,5]
# my_list = string.split()
# print(my_list)
# print(numbers)
# my_dict = {} # сщздаем словарь
# for i, key in enumerate(my_list): #ключ номер в словаре
#   my_dict[key] = numbers[i] # присваеваем ключу  значение 
# print(my_dict)


# # LAMBDA - это ананимная однострочная функция которая что-то возвращает

# operation = {'+' : lambda x, y: x + y, #словарь в качесте ключа операция(+,-,*,/) а в качестве значения функция(x + y, x-y и тд)
#              '-' : lambda x, y: x - y,                
#              '*' : lambda x, y: x * y,
#              '/' : lambda x, y: x / y}

# print(operation.get('+') (3,4))

# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет,
# зато искусственные спутники были запущены на круговые орбиты.
# Результатом функции должен быть кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты.
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения.
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса,
# а затем найти и сам эллипс, имеющий такую площадь.
# Гарантируется, что самая далекая планета ровно одна
import math
import random

planets = [(random.randint(1,10), random.randint(1,10)) for _ in range(10)]
print(f'Общий список планет с осями {planets}')

def orbit(planets: list):
  planets = list(filter(lambda x: x[0] != x[1], planets))
  print(f'Исключили планеты с равными осями {planets}')
  weight_planets = list(enumerate(map(lambda x: round(math.pi*x[0]*x[1], 2), planets), 1))
  print(f'Вес планет {weight_planets}')
  result = list(zip(planets, weight_planets))
  return result

all_planets = orbit(planets)

max_planets = all_planets[0]
for max_p in all_planets:
  if max_p[1][1] > max_planets[1][1]:
    max_planets = max_p

print(f'самая большая планета с индексом {max_planets[1][0]} массой {max_planets[1][1]} и осями {max_planets[0]}')