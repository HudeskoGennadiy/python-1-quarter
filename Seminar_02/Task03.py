# 3'. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
# Пример : 
# абвгдабвгд -> 2
# абв

print('Введите две строки ')

a = str(input())
b = str(input())

print(a.count(b))
