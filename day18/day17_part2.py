from collections import deque
# Crear una matriz de 70x70 llena de '.'
matriz = [['.' for _ in range(71)] for _ in range(71)]
col1=[]
col2=[]
i=0
k=1025
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

# Abrir el archivo y procesar sus líneas
with open('C:/Users/p.viñolas/Desktop/AoC/day17/day17.txt', 'r') as file:
    matrix=file
    for linea in matrix:
        partes = linea.strip().split(',')
        if len(partes) == 2: 
            izquierda, derecha = map(int, partes)  # Convertir a enteros
            col1.append(izquierda)
            col2.append(derecha)

while (1):
    m=0
    while m<k:
        matriz[col2[m]][col1[m]] = '#'
        m=m+1     
    inicio=(0,0)
    destino=(70,70)
    if matriz[inicio[1]][inicio[0]] == '#' or matriz[destino[1]][destino[0]] == '#':
        print("Error: El inicio o el destino están bloqueados.")
    camino=resolver_laberinto_bfs(matriz, inicio, destino)
    if camino==None:
        print(k)
        break
    k=k+1
print(col1[2874],col2[2874])


