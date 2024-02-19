'================Функия вышего порядка================='
# функция вышего порядка это функция которая принимает в аргументы другую 
# функцию и создает внутри себя другую функцию 
# вызывает функцию и врзвращает функцию
# def func1():
#     print 'hi'

# def func2(func_):
#     print_(func_())

# func2(func)

'======================Детораторы ============================='
# это функции высшего порядка которая нужна для расширения функцанала другой функции не изменяя ее (функция оберток)

# def decorator_glushitel(func):
#     def wrapper(args, **kwargs):
#        text = func(*args, **kwargs)
#        res = 'тихо ' + text
#        print(res)
#     return wrapper

# def gun():
#     print('стрелять')

# wrapper = decorator_glushitel(gun)
# wrapper() # способ использовать декторатор в ручную

# gun () # способ использования деторатор при помощи синтексического сахар

'----------------------------------------------------------------------'

# def decorator_glushitel(func):
#     def wrapper(args, **kwargs):
#        text = func(*args, **kwargs)
#        res = 'тихо ' + text
#        print(res)
#     return wrapper
# @decorator_glushitel
# def gun():
#     print('стрелять')


'-------------------------------------------------------------------'
# from datetime import datetime

# def decoraror(func):
#     def wrapper():
#         print('start:', datetime.now())
#         func()
#         print('finish:', datetime.now())
#     return wrapper

# def hello():
#     print('hello world')

# wrapper = decoraror(hello)
# wrapper()


'------------------------------------------------------------'
# def func_start_time(func):
#     def wrapper(*args, **kwargs):
#         print('start:',  datetime.now())
#         func(*args, **kwargs)
#     return wrapper

# @func_start_time
# def sum_(a, b):
#     print(a + b)

# sum_(20, 10)


'--------------------------------------------------------------------'
# def decorator(num):
#     def inner_decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(num):
#                 func(*args, **kwargs)
#         return wrapper
#     return inner_decorator

# @decorator(10)
# def hello():
#     print('hello world')

# hello()


def call_function(func):
    def wrapper(*args, **kwargs):
        print('Вызываю функцию', func.__name__)
        func()
        print('Вызов функции', func().__name__, 'прошел успешно')
    return wrapper






















