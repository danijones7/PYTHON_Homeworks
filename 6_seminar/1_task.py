# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент(a1), разность(d) и количество элементов(n) нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Input:
# 1 - a1
# 2 - d
# 5 - n
# Output:
# 1, 3, 5, 7, 9


def progressia(a, d, n):
    progressia = []
    for i in range(1, n+1):
        i = a + (i-1) * d 
        progressia.append(i)
    return progressia 

a = int(input("Введите первый элемент a: "))
d = int(input("Введите разность элементов d: "))
n = int(input("Введите количество элементов прогрессии n: "))

print(progressia(a,d,n))

