import math
print("Площадь вписанного в треугольник круга:")
a = 5
b = 7
c = 6
A = 90
p = ((a+b+c)/2)
print("Полупериметр:", (p)) 
Radius = (p-a)*(math.tan(A/2))
def circle(Radius):  
    area = Radius** 2 * math.pi 
    return area
#Radius = float(input("Введите радиус круга: "))
print("Площадь круга: ", circle(Radius))