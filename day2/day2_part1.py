datos=[]
cont=0
with open('C:/Users/p.viñolas/Desktop/AoC/day2/day2.txt', 'r') as archivo:
    for linea in archivo:
        linea = linea.strip()
        numeros = list(map(float, linea.split()))
        datos.append(numeros)
for linea in datos:
    i=0
    good=True
    safe=0
    while (i<len(linea)-1):
        if(linea[0]>linea[1]): #dsescendente
            if (linea[i]-linea[i+1]>3 or linea[i]-linea[i+1]<=0):
                good=False
                break
                
        elif(linea[0]<linea[1]): #asciende
            if (linea[i]-linea[i+1]<-3 or linea[i]-linea[i+1]>=0):
                good=False
                break
        else:
            good=False
            break
    

        i=i+1
    if good==True:
        cont=cont+1

print(cont)