'===== Переменные======'
"Переменные - это ссылкn на яйчейку памяти, где хранятся какие-то данные. Для дальнейшего использования"

name = 'Tima' 
age = 25

num1 = 15
num2 = 20
print(num1 + num2)

print('hello world')

'========Правила наименования переменных======='
a = 'tima' # можно но назначение не понятно 
# 1num = 12 - нельзя начинать переменные с чисел
# num-df = 13 - нельзя использовать символы кроме '_'
# hello world = 'hello world' - нельзя использовать пробелы в названии переменной
# print = 'print' - нельзя называть переменные встроенными словами из питона 

my_name = 'katana' 
# Snake case - python cтиль наименования переменных

# Camel case - стиль остальных языков программирования
MyName = 'katana'

'========Ввод и вывод данных======='
# print() - функция для ввывода данных в терминал
# input() - функция для ввода данных с терминала

print('makers')

name = input('Ведите ваше имя')

'========Типы данных======='
# Типы данных делятся на 2 вида: Изменяемые и неизменяемые

#Изменяемые типы данных:
list_ = [1,2,3, 'makers', True]
dict_ = {'a' :1, 'b' : 12, 'c': 0}
set_ = {1, 2, 313, 10, True}

#Неизменяемые типы данных:
int_ = 15
float_ = 0.5
complex_ = 5j
decimal_ = 0.5012030123
str_ = 'makers bootcamp'
tuple_ = (1, 2, 123, 0, -5)
boolean_1 = True
boolean_2 = False
none_type = None

num1 = 10
num2 = 5

print(num1 + num2) #сложение = 15
print(num1 - num2) #вычитание 5
print(num1 * num2) #умножение = 50
print(num1 / num2) #дробное денение = 2ю0
print(num1 // num2) #целечичленное деление =2
print(num1 % num2) #деление по остатку = 0
print(num1 ** num2) #возведение в степень = 100000
print(num1 ** 0.5) # корень числа
from math import sqrt
print(sqrt(num1)) #корень числа
print(abs(-num1)) # |-10| -> 10 модуль числа
print(round(5.6)) # 6 (округление в большую сторону)
print(round(5.4)) #5
print(round(5.5)) #6
print(round(5.49)) # 5 (округление идет только по первой цифре после точки)
print(pow(2,3)) # 2 3=8
print(pow(2,3,4)) # (2 3) % 4 = 0
#pow:
# 1. Возводит число в степень
# 2. Находит остаток от деления на 3 число
# divmod - функция ктороая возвращает 2 числа, где 1 - остаток от деления 
print(divmod(5,2)) # 8 % 4 = 0 # (2**3) % 4 = 0 # (2**3) % 4 = 0
print(divmod(5,2)) #2,1
print(divmod(17,3)) #5,2
#17 //3 = 52
#17 % 3 =2




