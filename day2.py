datos=[]
cont=0
with open('day2.txt', 'r') as archivo:
    for linea in archivo:
        linea = linea.strip()
        numeros = list(map(float, linea.split()))
        datos.append(numeros)
for linea in datos:
    i=0
    good=True
    safe=0
    while (i<len(linea)-1):
        if(linea[0]-linea[1]>0):
            if (linea[i]-linea[i+1]>3 or linea[i]-linea[i+1]<=0):          
                safe=safe+1
                if safe==2:
                    good=False
                    break

        elif(linea[0]-linea[1]<0):
            if (linea[i]-linea[i+1]<-3 or linea[i]-linea[i+1]>=0):
                safe=safe+1

                if safe==2:
                    good=False
                    break
        else:
            safe=safe+1
            if linea[1]-linea[2]<0:
                linea[0]=0
            else:
                linea[0]=100000
    

        i=i+1
    if good==True:
        cont=cont+1
print(cont)