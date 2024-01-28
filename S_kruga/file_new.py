print("Площадь вписанного в треугольник круга:")
a = float(input("Введите длину стороны a:"))
b = float(input("Введите длину стороны b:"))
c = float(input("Введите длину стороны c:"))
A = float(input("Введите угол A в градусах:"))
p = ((a+b+c)/2)
print("Полупериметр:", (p))
import math 
Radius = (p-a)*(math.tan(A/2))
def circle(Radius):  
    area = Radius** 2 * math.pi 
    return area
print("Площадь круга: ", circle(Radius))