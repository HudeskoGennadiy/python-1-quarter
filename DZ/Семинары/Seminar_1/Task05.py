# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# d = √ (х А – х В) 2 + (у А – у В) 2)
import math
print('Введите координаты точки А :')
xa = int(input())
ya = int(input())
print('Введите координаты точки B :')
xb = int(input())
yb = int(input())

d = math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)
print(round(d, 3))
