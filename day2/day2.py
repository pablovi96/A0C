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
        if(linea[0]>linea[1]): #dsescendente
            if (linea[i]-linea[i+1]>3 or linea[i]-linea[i+1]<=0):
                linea.pop(i+1)
                i=0
                safe=safe+1
                if safe==2:
                    good=False
                    break
                
        elif(linea[0]<linea[1]): #asciende
            if (linea[i]-linea[i+1]<-3 or linea[i]-linea[i+1]>=0):
                safe=safe+1
                linea.pop(i+1)
                i=0
                if safe==2:
                    good=False
                    break
        else:
            safe=safe+1
            if linea[1]<linea[2]:
                linea[0]=-11000
            elif linea[1]>linea[2]:
                linea[0]=100000
            else:
                good=False
                break
    

        i=i+1

    if good==True:
        cont=cont+1
    print(good)
print(cont)