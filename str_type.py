'===========String========='
#строки это неизменяемый тип данных который предназначен для хранения текста заключенного в одинарные либо двойные кавычки
string1 = 'строка с одинарными ковычками'
string2 = "строка с двойными ковычками"
# string3 = 'не правильная строка"
string4 = "Don't" # внутри двойной кавычки все одинарные - просто символы
string5 = ''' 
Многострочный текст в одинарных кавычках тут можно ставить 'любыe
 кавычки'''
string6 = 'hello' + 'world'
print(string6)
string7 = 'A' * 8
print(string7)
'====== Экранизация строк======'
'/n' # переносит текст на новую страку
print('hello\nworld')
#hello 
#world
'\t' # табуляция
print('hello\tworld')
#hello    world

str1 = 'don\'t' # отображает кавичку '
# print(str1)
str2 = "don\"t" 
print(str2)


str3 = 'Символ - \\'
print(str3)

'\v' # перенос на новую строку со смещением вправо на длину предудущей строки
print('hello\vworld\vmakers\vbootcamp')

'\r'   #перенос каретки на начало строки
print('Makers bootcamp\rHi')
# Hikers bootcamp
'===========Форматирование строк======='
#1
title = 'iphone14'
price = 150
format_1 = 'Мой телефон', title, 'стоит', price, 'долларов'
format_2 = f'Мой телефон {title} стоит {price}$'

print(format_2)
#2
string = 'Название: {} Цена: {}$'
print(string.format('iphone', 150))

#3
string = 'Название: %s Цена: %s'
print(string % ('iphone', 150))




'====================Методы строк============='
# методы - это функции, которые относятся к определенному классу, к ним можно обращщаться через точкую
print(dir(str))

string = 'makers'
print(string.upper()) # makers -> MAKERS 
print(string.lower()) #mMAKERS -> makers
print(string.swapcase()) #MaKErS -> mAkErs

print(string.title())# hello world -> Hello World


print(string.capitalize()) # hello world -> Hello world
print(string.center)(11, '-') #  '   ----hello ----  '
print(string.count('1')) # 'makers hello hello' -> 2

string = 'hello'
print(string.startswith('a')) #False
print(string.startswith('h'))#Tree
print(string.startswith('H')) # False
print(string.startswith('d')) # False
print(string.startswith('llo')) # True

string + 'makers'
print(string.islower)() #makers -> True
print(string.isupper()) #MAKERS -> True

string = '12345234'
print(string.isdigit()) # True проверка на цифры в тексте
print(string.isalpha()) # False - проверка на буквы в тексте

string = 'makers12345'
print(string.isalnum()) #True проверка на то что является ли строка с числами или с буквами или все вместе , но не символы.

string = 'hello.world.makers.bootcamp'
print(string)
print(string.split('.')) 


'================== Индексы=============='
# индекс это порядковый номер элемента в последовательности (символа в строке) , индексация начинается с 0

'h e l l o  w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
#              -3 -2 -1

string = 'hello world'
print(string[0]) # 'h'
print(string[7]) # 'o'
print(string[10]) #d
print(string[-1]) # 'd'

#срезы - подстрока (часть страки)
#string[start:end(не включительно):step]
string = 'hello world'
print(string[3:8]) # 'lo wo'
print (string[:]) # 'hello world'
print(string[6:])   # world
print(string[:5]) # hello
print(string[::-1]) # dlrow plleh
print(string[::2]) # hlowrd
print(string[::3]) # hlwl
print(string[::4]) # hor

string = 'hello'
string.upper() # hello -> HELLO
print(string)












