#5.Напишите программу, которая принимает на вход координаты двух точек 
#и находит расстояние между ними в 2D пространстве.
#Пример:
#A (3,6); B (2,1) -> 5,09
#A (7,-5); B (1,-1) -> 7,21

x1 = int(input('Введите координату X для первой точки A:\t'))
y1 = int(input('Введите координату Y для первой точки A:\t'))
x2 = int(input('Введите координату X для второй точки B:\t'))
y2 = int(input('Введите координату Y для второй точки B:\t'))

length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5)
print(f'Расстояние AB = {round(length,2)} между двумя точками.')