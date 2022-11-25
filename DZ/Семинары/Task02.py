# 2. Напишите программу для проверки истинности
#  утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('Введите значение x: ')
x = int(input())
print('Введите значение y: ')
y = int(input())
print('Введите значение z: ')
z = int(input())
left = not (x or y or z)
right = not x and not y and not z
result = left == right
print(result)
