while True:
    try:
        n=int(input("n="))
        if n>100:
            print("Ошибка, n не может превышать числа 100")
            continue
        break
    except:
        print("Ошибка")
        continue
print(((n**2)*((n+1)**2))/4)
for a in range(1, 11):
    for b in range(1, 11):
        print(f"{a*b:3}", end=" ")
    print()
