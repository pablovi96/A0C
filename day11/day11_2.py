n = []  
with open("C:/Users/p.viñolas/Desktop/AoC/day11/day11.txt", "r") as archivo:
    for linea in archivo:
       columnas=linea.split()
j=0
par=0
while j<40:
    i=0
    val=[]
    par=0
    while i<len(columnas):
        if columnas[i]=='0':
            val.append('1')
        elif len(columnas[i])%2==0:
            par=par+1
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
    print((val[0]))


# 11 15 23 37 53 78 125
# 4 8 14 16 25 