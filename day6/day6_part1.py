with open('C:/Users/p.viñolas/Desktop/AoC/day6/day6.txt', 'r') as archivo:
    texto=archivo.read()
data=[]
for fila in texto.splitlines():
    data.append(fila)
cont=0
fase='start'
i=-1
j=0
nc=len(data[0])
nf=len(data)
X=[]
while(1):
    #encontrar el empiece
    if fase=='start':
        i=i+1
        j=-1
        while j<nf-1:
            j=j+1
            if data[i][j]=='^':
                fase='up'
                break

    elif fase=='up':
        X.append([i,j])
        if data[i-1][j]=='#':
            fase='right'
            i=i+1
        i=i-1
    elif fase=='right':
        X.append([i,j])
        if data[i][j+1]=='#':
            fase='down'
            j=j-1
        j=j+1
    elif fase=='down':
        X.append([i,j])
        if i==nf-1:
            break
        if data[i+1][j]=='#':
            fase='left'
            i=i-1
        i=i+1

    elif fase=='left':
        X.append([i,j])
        if data[i][j-1]=='#':

            fase='up'
            j=j+1
        j=j-1


