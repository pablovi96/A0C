with open('C:/Users/p.viñolas/Desktop/AoC/day15/day15puzzle.txt', 'r') as archivo:
    texto=archivo.read()
data=[]
for fila in texto.splitlines():
    data.append(fila)
data = [list(row) for row in data]
i=0
for fila in data:
    j=0
    for element in fila:
        if element=='@':
           x=i
           y=j
           break
        j=j+1
    i=i+1
cont=0
with open('C:/Users/p.viñolas/Desktop/AoC/day15/day15.txt', 'r') as archivo:
    texto=archivo.read()

for order in texto:
    if order=='<':
        if data[x][y-1]=='.':
            data[x][y]='.'
            data[x][y-1]='@'
            y=y-1
        elif data[x][y-1]=='O':
            i=y-1
            while (1):
                
                if data[x][i]=='#':
                    break
                elif data[x][i]=='.':
                    data[x][i]='O'
                    data[x][y-1]='@'
                    data[x][y]='.'
                    y=y-1
                    break
                i=i-1
        

    elif order=='>':
            if data[x][y+1]=='.':
                data[x][y]='.'
                data[x][y+1]='@'
                y=y+1
            elif data[x][y+1]=='O':
                i=y+1
                while (1):
                    
                    if data[x][i]=='#':
                        break
                    elif data[x][i]=='.':
                        data[x][i]='O'
                        data[x][y+1]='@'
                        data[x][y]='.'
                        y=y+1
                        break
                    i=i+1
    
    elif order=='^':
        if data[x-1][y]=='.':
            data[x][y]='.'
            data[x-1][y]='@'
            x=x-1
        elif data[x-1][y]=='O':
            i=x-1
            while (1):
                
                if data[i][y]=='#':
                    break
                elif data[i][y]=='.':
                    data[i][y]='O'
                    data[x-1][y]='@'
                    data[x][y]='.'
                    x=x-1
                    break
                i=i-1
    elif order=='v':
        if data[x+1][y]=='.':
            data[x][y]='.'
            data[x+1][y]='@'
            x=x+1
        elif data[x+1][y]=='O':
            i=x+1
            while (1):
                
                if data[i][y]=='#':
                    break
                elif data[i][y]=='.':
                    data[i][y]='O'
                    data[x+1][y]='@'
                    data[x][y]='.'
                    x=x+1
                    break
                i=i+1
i=0
cont=0
for fila in data:
    j=0
    for element in fila:
        if element=='O':
           cont=cont+(100*i+j)
           print(i,j)
        j=j+1
    i=i+1
print(cont)
