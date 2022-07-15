#Площадь прямоугольного треугольника 
a = input("Введите 1 катет:")
b = input("Введите 2 катет:")
c = ""
n = 0
if not b == "":
    b = int(b)
if not a == "":
    a = int(a)
if b == "" or a == "":
    c = input("Введите гипотенузу")
    c = int(c)
    if c == "":
        print ("Найдите хотя-бы 2 стороны треугольника")
if not c == "" and a == "":
    n = c * c - b * b
if not c == "" and b == "":
    n = c * c - a * a
if not a == "" and not b == "":
    n = ((a * a) + (b * b))
print ("n * n =" + str(n))
