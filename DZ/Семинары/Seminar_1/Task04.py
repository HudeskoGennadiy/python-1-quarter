# 4. Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y).

print('Введите номер четверти: ')
fourth = int(input())

if fourth == 1:
    print('x > 0 & y > 0')
elif fourth == 2:
    print('x < 0 & y > 0')
elif fourth == 3:
    print('x < 0 & y < 0')
elif fourth == 4:
    print('x > 0 & y < 0')
else:
    print('Введите число от 1 до 4')
