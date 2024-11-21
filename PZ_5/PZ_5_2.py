#V 24
#2. Описать функцию RectPS(x1,y1,х2,y2,P, S), вычисляющую периметр P и площадь S
#прямоугольника со сторонами, параллельными осям координат, по координатам (х1, y1),
#(х2, y2) его противоположных вершин (x1, y1, x2, y2 — входные, P и S —
#выходные параметры вещественного типа). С помощью этой функции найти
#периметры и площади трех прямоугольников с данными противоположными вершинами.

def RectPS(x1, y1, x2, y2):
    a, b = abs(x2 - x1), abs(y2 - y1)
    P = 2 * (a + b)
    S = a * b
    return P, S

for i in range(3):
    x1, y1 = int(input("Введите x1: ")), int(input("Введите y1: "))
    x2, y2 = int(input("Введите x2: ")), int(input("Введите y2: "))
    P, S = RectPS(x1, y1, x2, y2)
    print(f"Периметр: {P}, Площадь: {S}")