from collections import deque

with open('C:/Users/p.viñolas/Desktop/AoC/day16/day16.txt', 'r') as archivo:
    texto=archivo.read()
data=[]
for fila in texto.splitlines():
    data.append(fila)
i=0
for fila in data:
    j=0
    for element in fila:
        if element=='S':
            x0=i
            y0=j
        elif element=='E':
            x1=i
            y1=j
        j=j+1
    i=i+1
inicio=(x0,y0)
destino=(1,139)

def resolver_laberinto_bfs(laberinto, inicio, destino):
    filas, columnas = len(laberinto), len(laberinto[0])
    cola = deque([(inicio, [inicio])])  # (posición actual, camino hasta ahora)
    visitados = set([inicio])

    while cola:
        (x, y), camino = cola.popleft()

        # Si llegamos al destino
        if (x, y) == destino:
            return camino

        # Explorar las direcciones
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] == '.' and (nx, ny) not in visitados:
                visitados.add((nx, ny))
                cola.append(((nx, ny), camino + [(nx, ny)]))



    return None  # No hay solución

# Ejemplo de uso
caminob = resolver_laberinto_bfs(data, inicio, destino)
i=1
direccion='L'
cont=0
while i<len(caminob):
    (x,y)=caminob[i-1]
    (x1,y1)=caminob[i]
    if y==y1 and direccion!='A':
        cont=cont+1000
        direccion='A'
    elif x==x1 and direccion!='L':
        cont=cont+1000
        direccion='L'
    i=i+1
cont=cont+i


        

print("Camino más corto encontrado:", cont)