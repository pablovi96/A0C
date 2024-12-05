col1=[]
col2=[]
with open('C:/Users/p.viñolas/Desktop/AoC/day5/day5.txt', 'r') as archivo:

    for linea in archivo:
        columnas = linea.split('|')
        col1.append(int(columnas[0]))
        col2.append(int(columnas[1]))

newData=[]
Final=[]
i=0
cont=False
cont2=False
n=0
with open('C:/Users/p.viñolas/Desktop/AoC/day5/day5_2.txt', 'r') as archivo:
    texto=archivo.read()
data=[]
for fila in texto.splitlines():
    numeros=[]
    for num in fila.split(','):
        numeros.append(int(num))
    data.append(numeros)
for fila in data:
    newData=fila.copy()
    i=0
    n=n+1
    while i<len(fila):
        j=0
        while j<len(col1):
            if fila[i]==col2[j]:
                k=i+1
                while k<len(fila):
                    if fila[k]==col1[j]:
                        cont=True
                        newData[i]= fila[k]
                        newData[k]= fila[i]
                        fila=newData.copy()
                        i=0
                        j=-1
                        break
                    k=k+1

        
            j=j+1
        i=i+1
    if cont==True:
        Final.append(newData)
        cont=False
res=0
n=0

for fila in Final:
    res=res+fila[int((len(fila)-1)/2)]


print (Final,res)

