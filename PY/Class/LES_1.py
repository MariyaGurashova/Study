"""
_______________________________________________________________
int - целое число
float - Дробные числа
bool  - Логический тип данных (True/False)
str - Строка
_______________________________________________________________

print(type(name)) - функция, которая указывает на тип данных

________________________________________________________________

Используйте разные кавычки для объявления переменной и внутри строки:
s = 'hello "world"'
s = "hello 'world'"
s = 'hello \"world'
_____________________________________________________________________

интерполяция
a = 3
b = 11
s = 2022
print(a, b, s)
print(a,'-'b,'-'s)
print('{} - {} - {}'.format(a,b,s))
print(f'first - {a} second - {b} third - {s}')
____________________________________________________________________

Приоритет арифметических операций
1. Возведение в степень (**)
2. Умножение (*)
3. Деление (/)
4. Целочисленное деление (//)
5. Остаток от деления (%)
6. Сложение (+)
7. Вычитание (-)
__________________________________________________________________

"""

print("Введите 1-е число ")
a = input()
print(type(a))
print("Введите 2-е число ")
b = input()
print(type(b))
# sum = int(a) + int(b)
# print(f"{a} + {b} = {sum}")
print(f"{a} + {b} = {int(a) + int(b)}")
print(type(print))