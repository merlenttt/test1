'======================Встроенные функции=========================='
# map, filter, reduce, zip, enumerate

'ZIP'
# соеденяет несколько последовательностей (получает генераторб в котором элементы - tuple) (zip object)

list_1 = [1, 2, 3, 4]
list_2 = ['a', ['b', 'c']]
list_3 = [10.5, 20.0, 1.3, 0.5]

zipped = zip(list_1, list_2, list_3)
print(zipped) #  <zip object at 0x7f8ajs23fs>
print(list(zipped)) 
print(dict(zipped)) # будет работать только с двумя листами в zip()

'ENUMERATE'
#нумерует последовательность ( по дефолту с 0)б (тоже возвращает генератор)
# < enumerate ogject 0x7kjf8392sjd90>

enumerated = enumerate('hello world', 100)
print(enumerated) # 
print(list(enumerated)) # [(0, 'h'), (1, 'e'), (2, '1')....]
for elem in enumerated:
    print(elem)

'MAP'
# принимает функцию и последовательность 
# записывает в новую последовательность результать функции , приминив ее на каждый элемент последовательности

list_ = ['1', '2', '3', '4']
mapped = map(int, list_) # <map object
print(list(mapped)) # [1, 2, 3, 4]
mapped2 = map() # [False, True, False, False]
print(list(mapped2))

list_ = [12, 34, 1, 2, 6]
def pow_(x):
    return x ** 2

print(list(map(pow_, list_)))
print(list(map(lambda x:x**2, list_)))

str_ = 'hello world'
mapped = map(str.upper, str_)
print(''.join(list(mapped)))

print(''.join(list(map(str.upper, 'hello world'))))

user = [
    {'name':'makers', 'age':20},
    {'name': 'anonym', 'age':15},
    {'name': 'sem', 'age':25}
]
 # оставить тех юзеров у которых возраст больше 18

# [{'name': 'sem', 'age' : 25}]

filtered = filter(lambda x: x ['name'].startswith('a'), users)
print(list(filtered))

'REDUCE'
# принимает функции и последовательность, возвращает 1 элемент (передаваемая функция должна принимать  2 аргумента)
# импортируется из functools

from functools import reduce
list_ = [1, 23,4, 1, 5, 10]
res = reduce(lambda x, y: x * y, list_)
print(res)

# 6
# 1


user = [
    {'name':'makers', 'age':20},
    {'name': 'anonym', 'age':15},
    {'name': 'sem', 'age':25}
]

# осставить тех юзеров у которых возраст большое 18 используя reduce

def func(x, y):
    if x['age'] < y['age']:
        return x
    else:
        return y
    
print(reduce(func, users))

res = reduce(lambda x, y: x if x<y else y, list_)
print(res)

def func(x,y):

    















































