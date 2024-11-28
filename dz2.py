import math
while True:
    try:
        a=float(input("Введите первое число a="))
        b=float(input("Введите второе число b="))
        c=a/b
        break
    except ValueError:
        print("Ошибка, это не число")
    except ZeroDivisionError:
        print("Ошибка, деление на ноль")
print(a,"/",b,"=",c)

while True:
    try:
        s=float(input("Введите сумму покупки: "))
        if s!=abs(s):
            print("Ошибка, отрицательное число")
            continue
        break
    except:
        print("Ошибка, это не число")
if s>20:
    s=s*0.65
print("Стоимость покупки =",s)

a={1:"Январь",2:"Февраль",3:"Март",4:"Апрель",5:"Май",6:"Июнь",7:"Июль",8:"Август",9:"Сентябрь",10:"Октябрь",11:"Ноябрь",12:"Декабрь"}
while True:
    try:
        g=int(input("Введите номер месяца: "))
        if g>12 or g<1:
            print("Ошибка, месяца с таким номером не существует")
            continue
        break
    except:
        print("Ошибка, это не число")
print("Это",a[g])
