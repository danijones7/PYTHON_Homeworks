# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

# Пример:
# Ввод: 13 -> 1, 2, 4, 8

N = int (input("Введите число N: "))
result = 0 
count = 0
while result <= N:
    result = 2 ** count
    if result <= N:
        count = count + 1
    else:
        break
    print (result)



# # Решение эталонное 

# n = int(input())
# i = 0
# while 2 ** i <= n:
# print(2 ** i)
# i += 1   