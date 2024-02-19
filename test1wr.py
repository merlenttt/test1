x = int(input("Введите первое число: ")) 
y = int(input("Введите второе число: ")) 
if x % y == 0: 
    print("x делится на y") 
    print("Частное:", x // y) 
else: 
    print("x не делится на y") 
    print("Частное:", x // y) 
    print("Остаток:", x % y)