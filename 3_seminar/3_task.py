# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 

# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# *Пример:*

# ноутбук
#     12

scrabbleeng_1 = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], 1)
scrabbleeng_2 = dict.fromkeys(['D', 'G'], 2)
scrabbleeng_3 = dict.fromkeys(['B', 'C', 'M', 'P'], 3)
scrabbleeng_4 = dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4)
scrabbleeng_5 = dict.fromkeys(['K',], 5)
scrabbleeng_8 = dict.fromkeys(['J', 'X'], 8)
scrabbleeng_10 = dict.fromkeys(['Q', 'Z'], 10)

scrabblerus_1 = dict.fromkeys(['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
scrabblerus_2 = dict.fromkeys(['Д', 'К', 'Л', 'М', 'П', 'У'], 2)
scrabblerus_3 = dict.fromkeys(['Б', 'Г', 'Ё', 'Ь', 'Я'], 3)
scrabblerus_4 = dict.fromkeys(['Й', 'Ы'], 4)
scrabblerus_5 = dict.fromkeys(['Ж', 'З', 'Х', 'Ц', 'Ч'], 5)
scrabblerus_8 = dict.fromkeys(['Ш', 'Э', 'Ю'], 8)
scrabblerus_9 = dict.fromkeys(['Ф', 'Щ', 'Ъ'], 10)

scrabble = {**scrabbleeng_1, **scrabbleeng_2, **scrabbleeng_3, **scrabbleeng_4, **scrabbleeng_5, **scrabbleeng_8, **scrabbleeng_10, 
            **scrabblerus_1, **scrabblerus_2, **scrabblerus_3, **scrabblerus_4, **scrabblerus_5, **scrabblerus_8, **scrabblerus_9}

slovo = input("Введите слово ЗАГЛАВНЫМИ буквами: ")  
result = 0
for i in slovo:
    if i in scrabble:
        result += scrabble[i]
print(f'Количество очков за слово {slovo}: {result}')