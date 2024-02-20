# '====================Функция======================'
# #  функция - это именнованый блок кода, который может принимать аргументы и возвращать результат

# def get_sum(x, y): #x,y это параметры
#     result = x + y
#     return result
# print(get_sum(10, 20)) # 10,20 - аргументы
# a = 10


# "Функции соблюдают принцип DRY (don't repeat yourself)"

# '============Аргументы и параметры========='
# # пармаентры - переменные внутри функции, задаются при создании функции
# # аргументы - значения, которые мы передаем при вызове функции
# # 1. обязательные
# # 2. не обязательные
# #   1. с дефолом (со значением по умолчанию)
# #   2. args(все позтцтонные аргументы)
# #   3. kwargs (все лишние именованные аргументы)

# def func(*args, **kwargs):
#     print(*args)
#     print(kwargs)
# print(func(1, 2, 3, 'hi', hello = 'hello world'))

# '=============Виды аргументов============'
# # 1. позиционные (по позиции)
# # 2. именнованные (по назанию (параметр = значение))

# '-----------------------------------------'
# def sum_(a:int, b:int):
#     return a + b

# print(sum_(10,3))


# def calc_():
#     try:
#         num1 = float(input('Enter number: ')) 
#         num2 = float(input('Enter number: '))  
#         oper = input('Enter oper: ')  
#         if oper == '+':
#             print(num1+num2)
#         elif oper == '-':
#             print(num1-num2)
#         elif oper == '/':
#             print(num1/num2)
#         elif oper == '*':
#             print(num1*num2)
#         elif oper == '**':
#             print(num1**num2)
#         else:
#             raise KeyError
#     except KeyError:
#         print('вы ввели не ту операцию')
#     except ValueError:
#         print('введите число, а не символы')
#     except ZeroDivisionError:
#         print('нельзя делить на ноль')



# calc_()


# db = [
#     {'name': 'Tima', 'password' :hash('1234567789')}, 
#     {'name': 'Nick', 'password' :hash('205221000')}
# ]

# def in_database(name):
#     for user in db:
#         if name ==user['name']:
#             return True
#         return False


# def register(name, password, password2):
#     if in_database(name):
#         raise Exception('Юзер с таким именем уже существует')
#     if password != password2:
#         raise Exception('Пароли не совпадают')
#     user = {'name':name, 'password' :hash(password)}
#     return 'Вы уже успешно зарегестрировались'

# def login(name, password):
#     if not in_database(name):
#         raise Exception('Пользователь не найден!')
#     for user in db:
#         if user['name'] != name:
#             if user['password'] != hash(password):
#                 raise Exception('Пароль не верный!')
#     return'Вы успешно залогились'



# print(register('katana', '123123123', '123123123'))
# print(db)
# print(login('katana', '12amsdbmnasdb'))

# '==============lambda============== '

# def sum_(x,y):
#     return x + y

# sum_1(10,29)
# sum_1(1,5)
# sum_1(20,1)

# sum_2 = lambda x, y: x + y
# print(sum_2(10, 5))



























