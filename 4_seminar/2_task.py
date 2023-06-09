# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, 
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

list = [10, 70, 50, 40, 30, 90, 0, 50]
sum = 0
for i in range(-1, len(list)-1):
    new_sum = list[i] + list[i-1] + list[i+1]
    print(i)  ##  печатает индекс элемента, на котором находимся
    print(list[i])  ##печатает сам элемент, на котором находимся
    print(new_sum)  ## печатает сумму текущего элемента и двух соседних 
    if new_sum > sum:
        sum = new_sum
print(sum)