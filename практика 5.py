# Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# РЕКУРСИЯ
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)

# number = int(input('введите число: '))
# i = 1
# fibo = []
# while i <= number:
#     fibo.append(fib(i))
#     i +=1
# print(fibo)

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# from random import randint
# grades = []
# for _ in range(10):
#     grades.append(randint(2,5)) #завели исходные оценки в журнале
# print(grades)

# for i in range(len(grades)):
#     if  grades[i] == max(grades):
#      grades[i] = min(grades)
# print(grades)

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# *Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)*

# number = int(input('введите число: '))

# def prime_number(num: int) -> bool:# заходит число интовое возвращает число булевое. int , bool можно не писать но это как подсказка для других прог-в
# #  if num % 2 == 0 and num != 2:
# #     return False
#  for i in range(3, num, 2): 
#     if num % i == 0:  
#         return('число не простое')
#     else:
#         return('число простое')

# print(prime_number(number))
