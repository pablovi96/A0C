import re
with open('day3.txt', 'r') as archivo:
    texto=archivo.read()
patron = r'mul\((\d+),(\d+)\)'  
res = re.findall(patron, texto)
cont=0
for linea in res:
    cont=cont+(int(linea[0])*int(linea[1]))
print (cont)
