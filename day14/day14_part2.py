import time
import numpy as np
from itertools import combinations

posiciones = []
velocidades = []


with open("C:/Users/p.viñolas/Desktop/AoC/day14/day14.txt", "r") as archivo:  
    for linea in archivo:
       
        partes = linea.strip().split()  
        p = partes[0].split("=")[1] 
        v = partes[1].split("=")[1]  
        
        posicion = tuple(map(int, p.split(",")))  
        velocidad = tuple(map(int, v.split(",")))  
        

        posiciones.append(posicion)
        velocidades.append(velocidad)

pos_end=posiciones.copy()
t=2000
k=False
mod=1000

while t<9000:
    cont=0
    i=0
    while i<len(posiciones):
        [x,y]=pos_end[i]
        x=x+velocidades[i][0]
        y=y+velocidades[i][1]

        if x<0:
            x=101+x
        elif x>=101:
            x=x-101
        if y<0:
            y=103+y
        elif y>=103:
            y=y-103
        pos_end[i]=[x,y]
        i=i+1
    
    # Retornar la distancia promedio
    pos=np.array(pos_end)
    media=np.std(pos[:,1])
    if media<mod:
        print(media)
        print(t)
        mod=media
        m, n = 101, 103 
        matriz = [['-' for _ in range(n)] for _ in range(m)]
        for x, y in pos_end:
            matriz[x][y] = 'X'

        for fila in matriz:
            print(" ".join(fila))

        t=t+1

