import os
with open("/home/juanes/Documents/UNAL/Ciencia_Datos/LAB/lab1/data.csv", "r") as file:
        data = file.readlines()
data = [line.replace("\n", "") for line in data]
data = [line.split("\t") for line in data]
mapl = []
dat2 =[]
for value in data:
    tup1 = value
    str1 = tup1 [4]
    dat1 = str1.split(",")
    for val in dat1:
        dat2 = val.split(":")
        tupa1 = value[0], dat2[1]
        mapl.append(tupa1)
mapl.sort(reverse=False)
print (mapl)
def reducer(sequence):
    x = 0
    reduce1 = []
    while x < len(sequence):
    #for x in range(len(mapl)):
        #print (x)
        tup1 = sequence[x]
        key1 = tup1[0]
        count = int(tup1[1])
        #print (count)
        y = x
        bolx = True
        while (bolx == True):
            #print(key1)
            if (x+1 == len(sequence)):
                x = x+1
                break
            tup2 = sequence[x+1]
            key2 = tup2[0]
            if key1 == key2:
                count = count + int(tup2[1])
                #print (count)
                x = x+1
            else:
                bolx = False
                x = x+1

        tup = tuple()
        tup = key1, count
        reduce1.append(tup)
    return reduce1
result = reducer(mapl)
print (result)