num = []  
with open("C:/Users/p.viñolas/Desktop/AoC/day9/day9.txt", "r") as archivo:
    n=archivo.read()
i=0

n2=[]
cont=0
while i<len(n):
    k=0
    while k<int(n[i]):
        if i%2==0:
            if i==0:
                n2.append(i)
            else:
                n2.append(int(i/2))

        else:
            n2.append('.')
            cont=cont+1
        k=k+1
    i=i+1
j=len(n2)-1
n3=[]
cont2=0
i=0
while i<len(n2):
    if n2[i]!='.':
        n3.append(n2[i])
    else:
        while j>0:
            if n2[j]=='.':
                j=j-1
            else:
                n3.append(n2[j])
                j=j-1
                break
    if i>=j:
        break
    i=i+1
i=0
cont=0
print(n3)
while i<len(n3):
    cont=cont+i*n3[i]
    i=i+1
print(cont)