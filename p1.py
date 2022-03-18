import os
with open("/home/juanes/Documents/UNAL/Ciencia_Datos/LAB/lab1/data.csv", "r") as file:
        data = file.readlines()
data = [line.replace("\n", "") for line in data]
data = [line.split("\t") for line in data]
suma = 0
for x in data:
    suma =  int(x[1]) + suma
print (suma)

mapl = []
for value in data:
    tup1 = value
    str1 = tup1 [0]
    tupa = str1,1
    mapl.append(tupa)
    mapl.sort(reverse=False)
print (mapl)
