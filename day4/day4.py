import re
import pandas as pd
with open('C:/Users/p.viñolas/Desktop/AoC/day4/day4.txt', 'r') as archivo:
    texto=archivo.read()
data=[]
for fila in texto.splitlines():
    data.append(fila)

nf=len(data)
nc=len(data[0])
i=0
j =0
cont=0
print(nf,nc)
while i<nc:
    j=0
    while j<nf:
        if data[i][j]=='X':
            if i<nf-3:
                if (data [i][j]+data [i+1][j]+data [i+2][j]+data [i+3][j]=='XMAS'):
                    cont=cont+1
            if i>2:
                if (data [i][j]+data [i-1][j]+data [i-2][j]+data [i-3][j]=='XMAS'):
                    cont=cont+1
            if j>2: 
                if (data [i][j]+data [i][j-1]+data [i][j-2]+data [i][j-3]=='XMAS'):
                    cont=cont+1
            if j<nf-3:
                if (data [i][j]+data [i][j+1]+data [i][j+2]+data [i][j+3]=='XMAS'):
                    cont=cont+1
            if j>2 and i>2:
                if (data [i][j]+data [i-1][j-1]+data [i-2][j-2]+data [i-3][j-3]=='XMAS'):
                    cont=cont+1
            if j<nc-3 and i>2:
                if (data [i][j]+data [i-1][j+1]+data [i-2][j+2]+data [i-3][j+3]=='XMAS'):
                    cont=cont+1
            if j<nc-3 and i<nf-3:
                if (data [i][j]+data [i+1][j+1]+data [i+2][j+2]+data [i+3][j+3]=='XMAS'):
                    cont=cont+1
            if j>2 and i<nf-3:
                if (data [i][j]+data [i+1][j-1]+data [i+2][j-2]+data [i+3][j-3]=='XMAS'):
                    cont=cont+1
        j=j+1
    i=i+1
print(cont)