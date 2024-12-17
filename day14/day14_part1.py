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
t=0
while t<100:
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
    t=t+1



j=0
cont1=0
cont2=0
cont3=0
cont4=0
print(pos_end)
while j<len(pos_end):
    [x,y]=pos_end[j]
    if x<50 and y<51:
        cont1=cont1+1
    elif x>50 and y <51:
        cont2=cont2+1
    elif x<50 and y>51:
        cont3=cont3+1
    elif x>50 and y>51:
        cont4=cont4+1
    j=j+1
print(cont1,cont2,cont3,cont4)
