import re
import pandas as pd
with open('C:/Users/p.viñolas/Desktop/AoC/day4/day4.txt', 'r') as archivo:
    texto=archivo.read()
data=[]
for fila in texto.splitlines():
    data.append(fila)

nf=len(data)
nc=len(data[0])
i=1
j =0
cont=0
cont2=0
print(nf,nc)
while i<nc-1:
    j=1
    while j<nf-1:
        cont=0
        if data[i][j]=='A':
            if (data [i-1][j-1]+data [i][j]+data [i+1][j+1]=='MAS'):
                    cont=cont+1
            if (data [i+1][j+1]+data [i][j]+data [i-1][j-1]=='MAS'):
                    cont=cont+1 
            if (data [i+1][j-1]+data [i][j]+data [i-1][j+1]=='MAS'):
                    cont=cont+1
            if (data [i-1][j+1]+data [i][j]+data [i+1][j-1]=='MAS'):
                    cont=cont+1
            if cont==2:
                  cont2=cont2+1
        j=j+1
    i=i+1
print(cont2)