import os

##def read_last(lines,file):
##    if not isinstance(lines,int) or lines<=0:
##        return("Ошибка в количестве строк")
##    p=open(file,encoding="utf-8")
##    p1=p.readlines()
##    for i in range(lines):
##        print(p1[i].replace("\n",""))

##def print_docs(directory):
##        s=os.walk(directory)
##        for a,b,c in s:
##                print("содержимое папки",a)
##                for i in b+c:
##                        print(i)
## 
##print_docs(r"C:\Users\bugae\OneDrive\Документы\GitHub\-")


##def longest_words(file):
##        b=[]
##        p=open(file,encoding="utf-8")
##        p1=p.read()
##        s=p1.split()
##        a=max(len(i) for i in s)
##        for i in s:
##                if len(i)==a:
##                        b.append(i)
##        return b

n=str(input("имя будущего файла: "))+".txt"
f=open(n,"w",encoding="utf-8")
while True:
        a=input()
        if not a:
                break
        f.write(a+"\n")
f.close()
