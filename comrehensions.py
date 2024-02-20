# '====================Comprehensions===================='
# # Генератор, с помощью которого мы можем создавать последовательности используя цикл for в одну строку

# # елемент for елемент in послеедовательность
# # елемент for елемент in послеедовательность if фильтр
# # елемент1 if условие1 else елемент2 for елемент in последовательность

# compr_ = [i for i in range(6)
#     print(compr_)]

# compr_1 = []
# for i in range(6)
#     ----

# # list_ =[12,None, hi, 123, 1,6,2,True, 0, False]

# # new_list_ = [[i for i in list_ if bool (i)]]
# # print(new_list_)

# # new_list_2 = 2[i if bool (i) else 0 for i in list_]
# # print(new_list_2)

# # new_list_2 = []
# # for i in list_:
# #     if bool(i)
# #         new_list_2.append(i)
# #     else:
# #         new_list_2.append(0)
# # print(new_list_2)
    

# list_ = [12,3,0,34,9,7]
# new_list_ = --



# list_ = [1, 'hi' , 123, 'hello world', True, 'makers', False]

# new_list_2 = []
# for i in list_:
#     if type(i) == str:
#         new_list_2.append(i)

# new_list = [i for i in list_ if type(i) == str]
# print(new_list)



# '===================Виды comprehension=================='
# # list comprehension -> []
# # dict comprehension -> {:}
# # set comprehension -> {}
# # comprehension генератор -> ()
# compr_ = (i for i in range(11))
# print(compr_)
# 'DICT COMPREHENSION'
# {1:1, 2:4, 3:9, 4:16}

# dict_ = {i:i**2 for i in range(1,5)}
# print(dict_)

# {'a':1, 'b':2, 'c':3}
# new_dict_ ---

# new_dict_2 = {v**2:v for v in dict_.values()}
# print(new_dict_2)

# 'SET_COMPREHENSION'
# set_ ={i for i in range (11) if i %2 == 0}
# print(set_)


# set_1 = {12, 34, 1, 'hi', 'hello', 123, 'None'}
# print(set_1)
# set2 ={i for i in set_1 if type (i)  == str}
# print(set2) # { 'HELLO', 'HI'}

'====================Вложеные comprehension======================'

# создайте словарь где ключами будут списки числа от 1 до 5 а значениями списки с числами от 1 до этого числа
dict_ = {}
for i in range(1,6):
    key = i
    values = [j for j in range(1, i+1)] # 1,2
    dict_[key] = values


dict_ = {i: [j for j in range(1, i+1)] for i in range(1,6)}

i = i +1 # i+=1 






















































