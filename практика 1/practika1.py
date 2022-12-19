#1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# num1 = int(input('введите первое число : '))
# num2 = int(input('введите второе число : '))

# if num1 == num2**2:
#      print(f'{num2} является квадратом {num1}')
# elif num2 == num1**2:
#     print(f'{num1} является квадратом {num2}')
# else:
#     print('числа не являются квадратами друг друга')

#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
my_list = []
for i in range(5):
     my_list.append(int(input(f'введите {i+1} число: ')))
     my_max = my_list[0]
     for item in (my_list):  
        if my_max < item:
            my_max = item 
            #или
    #         my_max = my_list[0]
    #  for i in range (1, len(my_list)):  
    #     if my_max < my_list[i]:
    #         my_max = my_list[i] 
print(f'максимальное значение списка {my_max}')

# for range in my_list: #пробегается по индексам
#     print(my_list[i])

