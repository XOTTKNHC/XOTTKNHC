import random
##a=[[random.randint(-10,10) for i in range(3)] for i in range(3)]
##print(max(i[2] for i in a:))

##n=int(input("n="))
##m=int(input("m="))
##a=[[random.randint(-10,10) for i in range(n)] for i in range(m)]
##print(a)
##print([[1 if i>0 else 0 for i in b] for b in a])


##n=int(input("n="))
##a=[[random.randint(-10,10) for i in range(n)] for i in range(n)]
##a=[
##    [4, 9, 2],
##    [3, 5, 7],
##    [8, 1, 6]
##    ]
##print(a)
##flag=True
##aa=sum(a[0])
##for i in range(len(a)):
##    s=0
##    if sum(a[i])!=aa:
##        flag=False
##    for j in range(len(a)):
##        s+=a[j][i]
##    if s!=aa:
##        flag=False
##print(flag)

##n=int(input("n="))
##a=[[random.randint(-10,10) for i in range(n)] for i in range(n)]
##a=[
##    [1, 2, 3],
##    [2, 4, 5],
##    [3, 5, 6]
##    ]
##flag=True
##for i in range(len(a)):
##    for j in range(len(a)):
##        print(a[i][j],a[j][i])
##        if a[i][j]!=a[j][i]:
##            flag=False
##print(flag)

##n=int(input("n="))
###a=[[int(input()) for i in range(n)]for i in range(n)]
##a=[
##    [1, 2, 3],
##    [2, 4, 5],
##    [3, 5, 6]
##    ]
##print(a)
##
##s1=-10**10
##s2=10**10
##for i in range(len(a)):
##    s=sum(a[i])
##    s1=max(s1,s)
##    s2=min(s2,s)
##    if s==s1:
##        b1=a[i]
##    if s==s2:
##        b2=a[i]
##print(s1,b1)
##print(s2,b2)

##n=int(input("n="))
###a=[[random.randint(-10,10) for i in range(n)] for i in range(n)]
##a=[
##    [1, 2, 3],
##    [2, 4, 5],
##    [3, 5, 6]
##    ]
##print(a)
##for i in range(len(a)):
##    if a[i][a[i].index(min(a[i]))]%2==0:
##        a[i][a[i].index(min(a[i]))]=0
##    else:
##        a[i][a[i].index(min(a[i]))]=1

