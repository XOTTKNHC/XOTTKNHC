##import math
##def dz1():
##    x1=float(input("x1="))
##    x2=float(input("x2="))
##    y1=float(input("y1="))
##    y2=float(input("y2="))
##    z1=float(input("z1="))
##    z2=float(input("z2="))
##    a=[(x1,x2),(y1,y2),(z1,z2)]
##    b=[ugol(x1,x2),ugol(y1,y2),ugol(z1,z2)]
##    return a[b.index(min(b))]
##def ugol(x,y):
##    ugl=math.atan2(y,x)
##    if ugl<0:
##        ugl=ugl+2*math.pi
##    return ugl
##print("координаты точки, для которой угол между осью абсцисс и лучом, соединяющим начало координат с точкой, минимальный:",dz1())

def prost(n):
    if n <= 1:  
        return False
    for i in range(2,int(n**0.5)+1):  
        if n%i==0:
            return False
    return True
n=int(input("n="))
k=0
for i in range(n):
    if prost(i):
        if bin(i)[2:]==bin(i)[2:][::-1]:
            k+=1
            print(bin(i)[2:],i)
print(k)
