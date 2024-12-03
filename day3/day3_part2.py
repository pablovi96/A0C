import re
with open('C:/Users/p.viñolas/Desktop/AoC/day3/day3.txt', 'r') as archivo:
    texto=archivo.read()

i=0
lect=1
newText=[]
while (i<len(texto)):
    if texto[i:i+4]=='do()':
        i=i+3
        lect=1
    if texto[i:i+7]=="don't()":
        i=i+5
        lect=0
        print (lect)
    if lect==1:
        newText.append(texto[i])
    i=i+1
T = ''.join(newText)
patron = r'mul\((\d+),(\d+)\)'  
res = re.findall(patron, T)
cont=0
for linea in res:
    cont=cont+int(linea[0])*int(linea[1])
print (cont)