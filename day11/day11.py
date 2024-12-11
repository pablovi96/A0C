n = []  
with open("C:/Users/p.viñolas/Desktop/AoC/day11/day11.txt", "r") as archivo:
    for linea in archivo:
       columnas=linea.split()
j=0
while j<25:
    i=0
    val=[]
    while i<len(columnas):
        if columnas[i]=='0':
            val.append('1')
        elif len(columnas[i])%2==0:
            mid=int(len(columnas[i])/2)
            x=int(columnas[i][0:mid])
            y=int(columnas[i][mid:len(columnas[i])])

            val.append(str(x))
            val.append(str(y))
        else:

            x=int(columnas[i])*2024
            val.append(str(x))
        i=i+1
    columnas=[]
    columnas=val.copy()
    j=j+1
print(len(val))