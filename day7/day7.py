num = []  
valores = []  

with open("C:/Users/p.viñolas/Desktop/AoC/day7/day7.txt.txt", "r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        nume, valores_linea = linea.split(':')
        num.append(int(nume))
        valores.append(list(map(int, valores_linea.split())))
i=0
for  j in range(len(valores[i])):
    