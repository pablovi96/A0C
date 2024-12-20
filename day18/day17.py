from collections import deque
# Crear una matriz de 70x70 llena de '.'
matriz = [['.' for _ in range(71)] for _ in range(71)]
col1=[]
col2=[]
i=0
with open('C:/Users/p.viñolas/Desktop/AoC/day17/day17.txt', 'r') as archivo:
    for fila in archivo:
        col=fila.split(',')
        matriz[int(col[1])][int(col[0])] = '#'
        i=i+1
        if i==1024:
            break
       
inicio=(0,0)
destino=(70,70)
if matriz[inicio[1]][inicio[0]] == '#' or matriz[destino[1]][destino[0]] == '#':
    print("Error: El inicio o el destino están bloqueados.")
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

camino=resolver_laberinto_bfs(matriz, inicio, destino)



print("Camino más corto encontrado:", len(camino))