# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# # Пример:- 6782 -> 23
# #        - 0,56 -> 11
#
# number1 = input('введите число: ')  # просим ввести число
# delete_point = number1.replace('.', '')  # c помощью replace убираем знак точки в числе
# convert_to_list = list(delete_point)  # превращаем наше число в список
# convert_to_int = map(int, convert_to_list)  # c помощью функции map мы присваеваем числовое значение
# add_up_the_numbers = sum(convert_to_int)  # с помощью функции sum складываем все числа слева направо
# print(add_up_the_numbers)  # печатаем результат

# # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# # пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4
#
# number_of_iterations = int(input('введите число: '))
# count = 1
# for i in range(number_of_iterations):
#     count = count * (i + 1)
#     print(count)

# # Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# #
# # Пример: - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
#
number = int(input('input number: '))
summa = 0
for i in range(1, number + 1):
    count = (1 + 1 / i) ** i
    print(f'{i}:{"%.2f" % count}')
    summa += count

print(f'total: {"%.2f" % summa}')



