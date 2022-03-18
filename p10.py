import os
with open("/home/juanes/Documents/UNAL/Ciencia_Datos/LAB/lab1/data.csv", "r") as file:
        data = file.readlines()
data = [line.replace("\n", "") for line in data]
data = [line.split("\t") for line in data]
mapl = []
dat2 =[]
for value in data:
    tup1 = value
    str1 = tup1 [0]
    col4 = tup1 [3]
    col5 = tup1[4]
    dat1 = col4.split(",")
    dat2 = col5.split(",")
    tupa = str1, len(dat1), len(dat2)
    mapl.append(tupa)
print (mapl)
