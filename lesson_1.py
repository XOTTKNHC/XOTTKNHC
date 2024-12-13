import math
r=int(input("Введите значение r: "))
print("Длина кружности равна",round(2*math.pi*r,2),"\nПлощадь круга равна",round(math.pi*(r**2),2))
x=10
y=55
print(x,y)
x,y=y,x
print(x,y)
g=9.81
l=float(input("Введите значение l"))
print(round(2*math.pi*((l/g)**0.5),2))
n1=float(input("n1="))
n2=float(input("n2="))
if n2==0:
    print("Ошибка, деление на ноль")
else:
    print("n1/n2=",n1/n2)
