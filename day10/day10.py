datos = []
i=0 
with open("C:/Users/p.viñolas/Desktop/AoC/day10/day10.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        datos.append(linea)
nf=len(datos)
nc=len(datos[0])
res=0
otra=False
while i<nf:
    j=0
    while j<nc:
        if datos[i][j]=='0':
            x=0
            k=i
            l=j
            cont=0
            if otra==False:
                camino=[0,0,0,0,0,0,0,0,0]
            else:
                otra=False
            while x!=9:
                if k<nc-1 and datos[k+1][l]==str(x+1) and camino[cont]!=1:
                    x=x+1
                    k=k+1
                    camino[cont]=1
                elif l<(nf-1) and datos[k][l+1]==str(x+1)and camino[cont]!=2:
                    x=x+1 
                    l=l+1
                    camino[cont]=2

                elif datos[k-1][l]==str(x+1)and camino[cont]!=3:
                    x=x+1
                    k=k-1
                    camino[cont]=3

                elif datos[k][l-1]==str(x+1)and camino[cont]!=4:
                    x=x+1
                    l=l-1
                    camino[cont]=4
                else:
                    break

                cont=cont+1

                if x==9:
                    print(camino)
                    otra==True
                    res=res+1

        j=j+1
    i=i+1
print(res)
            