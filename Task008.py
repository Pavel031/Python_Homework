# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Введите координаты по оси X: '))
y = int(input('Введите координаты по оси Y: '))

if x>0 and y>0:
    print("точка находится в 1 четверти плоскости")
if x<0 and y>0:
    print("точка находится во 2 четверти плоскости")
if x<0 and y<0:
    print("точка находится в 3 четверти плоскости")
if x>0 and y<0:
    print("точка находится в 4 четверти плоскости")
if x==0:
    print("точка находится на оси Y")
if y==0:
    print("точка находится на оси X")
if x==0 and y==0:
    print("точка находится в начале координат")