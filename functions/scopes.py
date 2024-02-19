'==================Облости видимости================'
#LEGB - local enclosed global build - in

'=================Build - in========================'
# встроенные пространство имен (list, print, dict, len, input)

'===================Global======================'
# все переменные , которые мы создали внутри файла 
# чтобы посмотреть все глобальные переменные, можно использовать функцию globals
# a = 10
# b = 'hello'
# print(globals())
'====================enclosed==============='
# замкнутое пространство имен- это локальное пространство, у которого есть внутренее локальное пространство

# var = 'global' # хранится в глобальном пространстве
# def func():
#     var = 'enclosed'
#     def inter_func():
#         var = 'local'
#         print(var)
#     print(var)
#     inter_func()
# print(var)
# func()

'======================Local===================='
# локальное пространство имен - это пространство которoе находится внутри функции

# a = 10
# def func(a, b):
#     res = a + b
#     print(res)
#     print(locals())


# func(10, 5)

# count = 1
# def count_():
#     count += 1
#     global count
#     print(count)


# def func():
#     print('hello world')
#     return func

# func()()()()()






