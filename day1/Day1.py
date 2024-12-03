col1 = []
col2 = []

with open('./day1.txt', 'r') as archivo:
    for linea in archivo:
        columnas = linea.split()
        col1.append(int(columnas[0]))
        col2.append(int(columnas[1]))

left = []
right = []

s = 0
while s < len(col1):
    max1 = max(col1)
    max2 = max(col2)
    
    left.append(max1)
    right.append(max2)
    
    col1[col1.index(max1)] = 0
    col2[col2.index(max2)] = 0
    
    s = s+1
x=0
cont=0
while (x<len(col1)):
    cont=cont+abs(left[x]-right[x])
    x=x+1
print(cont)
