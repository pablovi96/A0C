col1 = []
col2 = []

with open('./day1.txt', 'r') as archivo:
    for linea in archivo:
        columnas = linea.split()
        col1.append(int(columnas[0]))
        col2.append(int(columnas[1]))
sim=0
i=0
while i<len(col1):
    j=0
    cont=0
    while j<len(col1):
        if col1[i]==col2[j]:
            cont=cont+1
        j=j+1
    sim=sim+(col1[i]*cont)
    i=i+1
print(sim)
