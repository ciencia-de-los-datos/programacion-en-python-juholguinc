"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
global data
with open("data.csv", "r") as file:
    data = file.readlines()
data = [line.replace("\n", "") for line in data]
data = [line.split("\t") for line in data]


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    suma = 0
    for x in data:
        suma = int(x[1]) + suma
    #print(suma)
    return suma

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    mapl = []
    for value in data:
        tup1 = value
        str1 = tup1[0]
        tupa = str1, 1
        mapl.append(tupa)
    mapl.sort(reverse=False)
    #print(mapl)
    result = reducer_cant(mapl)
    return result

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    mapl = []
    for value in data:
        tup1 = value
        str1 = tup1[0]
        tupa = str1, str(tup1[1])
        mapl.append(tupa)
    mapl.sort(reverse=False)
    #print(mapl)
    result = reducer_sum(mapl)
    return result

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    mapl = []
    for value in data:
        tup1 = value
        str1 = tup1[2]
        str2 = str1[5] + str1[6]
        tupa = str2, 1
        mapl.append(tupa)
    mapl.sort(reverse=False)
    result = reducer_cant(mapl)
    return result

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    mapl = []
    for value in data:
        tup1 = value
        str1 = tup1[0]
        tupa = str1, str(tup1[1])
        mapl.append(tupa)
    mapl.sort(reverse=False)
    result = reducer_max_min(mapl)
    return result

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    mapl = []
    dat2 = []
    for value in data:
        tup1 = value
        str1 = tup1[4]
        dat1 = str1.split(",")
        for val in dat1:
            dat2.append(val)
    for val in dat2:
        # dat2 = dat1[0]
        dat3 = val.split(":")
        str2 = dat3[0]
        tupa = str2, int(dat3[1])
        mapl.append(tupa)
    mapl.sort(reverse=False)
    result = reducer_min_max(mapl)
    return result

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    mapl = []
    for value in data:
        tup1 = value
        int1 = int(tup1[1])
        tupa = int1, tup1[0]
        mapl.append(tupa)
    #mapl.sort(reverse=False)
    #print(mapl)
    result = reducer_tup2(mapl)
    return result

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    mapl = []
    for value in data:
        tup1 = value
        int1 = int(tup1[1])
        tupa = int1, tup1[0]
        mapl.append(tupa)
        mapl.sort(reverse=False)
    #print(mapl)
    result = reducer_u_tup(mapl)
    return result

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    mapl = []
    dat2 = []
    for value in data:
        tup1 = value
        str1 = tup1[4]
        dat1 = str1.split(",")
        for val in dat1:
            dat2.append(val)
    for val in dat2:
        # dat2 = dat1[0]
        dat3 = val.split(":")
        str2 = dat3[0]
        tupa = str2, int(dat3[1])
        mapl.append(tupa)
    mapl.sort(reverse=False)
    result = reducer_cant(mapl)
    diction = {}
    dictionary = Convert1(result, diction)

    return dictionary

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    mapl = []
    dat2 = []
    for value in data:
        tup1 = value
        str1 = tup1[0]
        col4 = tup1[3]
        col5 = tup1[4]
        dat1 = col4.split(",")
        dat2 = col5.split(",")
        tupa = str1, len(dat1), len(dat2)
        mapl.append(tupa)
    return mapl

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    mapl = []
    dat2 = []
    for value in data:
        tup1 = value
        str1 = tup1[3]
        dat1 = str1.split(",")
        for val in dat1:
            tupa1 = val, tup1[1]
            mapl.append(tupa1)
    mapl.sort(reverse=False)
    result = reducer_sum(mapl)
    dic = {}
    diction = Convert1(result, dic)
    return diction

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    mapl = []
    dat2 = []
    for value in data:
        tup1 = value
        str1 = tup1[4]
        dat1 = str1.split(",")
        for val in dat1:
            dat2 = val.split(":")
            tupa1 = value[0], dat2[1]
            mapl.append(tupa1)
    mapl.sort(reverse=False)
    result = reducer_sum(mapl)
    dic = {}
    diction = Convert1(result, dic)
    return diction

# funcion de conteo para pregunta 2
def reducer_cant(sequence):
    x = 0
    reduce1 = []
    while x < len(sequence):
    #for x in range(len(mapl)):
        #print (x)
        count = 1
        tup1 = sequence[x]
        key1 = tup1[0]
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
                count = count + 1
                x = x+1
            else:
                bolx = False
                x = x+1

        tup = tuple()
        tup = key1, count
        reduce1.append(tup)
    return reduce1

# funcion de suma para pregunta 3
def reducer_sum(sequence):
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

# funcion maximo minimo pregunta 5
def reducer_max_min(sequence):
    x = 0
    reduce1 = []
    while x < len(sequence):
    #for x in range(len(mapl)):
        #print (x)
        tup1 = sequence[x]
        key1 = tup1[0]
        count = int(tup1[1])
        #print (key1)
        mayor = count
        menor = count
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
                count2 = int(tup2[1])
                if count2 <= menor:
                    menor = count2
                else:
                    mayor = count2
                #print (count2)
                count = count2
                x = x+1
            else:
                bolx = False
                x = x+1

        tup = tuple()
        tup = key1, mayor, menor
        reduce1.append(tup)
    return reduce1

# funcion minimo maximo pregnta 6
def reducer_min_max(sequence):
    x = 0
    reduce1 = []
    while x < len(sequence):
    #for x in range(len(mapl)):
        #print (x)
        tup1 = sequence[x]
        key1 = tup1[0]
        count = int(tup1[1])
        #print (key1)
        mayor = count
        menor = count
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
                count2 = int(tup2[1])
                if count2 <= menor:
                    menor = count2
                else:
                    mayor = count2
                #print (count2)
                count = count2
                x = x+1
            else:
                bolx = False
                x = x+1

        tup = tuple()
        tup = key1, menor, mayor
        reduce1.append(tup)
    return reduce1

#Funcion tupla pregunta 7
def reducer_tup(sequence):
    x = 0
    reduce1 = []
    while x < len(sequence):
    #for x in range(len(mapl)):
        #print (x)
        tup1 = sequence[x]
        key1 = tup1[0]
        count = []
        count.append(tup1[1])
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
                count.append(tup2[1])
                #rint (count)
                x = x+1
            else:
                bolx = False
                x = x+1

        tup = tuple()
        tup = key1, count
        reduce1.append(tup)
    return reduce1

#Funcion tupla pregunta 7
def reducer_tup2(sequence):
    x = 0
    reduce1 = []
    uni = []
    for x in sequence:
        tup = x
        keys = tup[0]
        uni.append(keys)
    uni = unique(uni)
    uni.sort(reverse=False)
    for y in uni:
        lis = []
        for x in sequence:
            if y == x[0]:
                lis.append(x[1])
        tupa = tuple()
        tupa = y, lis
        reduce1.append(tupa)
    return reduce1

# Reducer unique pregunta 8
def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
    # print list
def reducer_u_tup(sequence):
    x = 0
    reduce1 = []
    while x < len(sequence):
    #for x in range(len(mapl)):
        #print (x)
        tup1 = sequence[x]
        key1 = tup1[0]
        count = []
        count.append(tup1[1])
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
                count.append(tup2[1])
                #rint (count)
                x = x+1
            else:
                bolx = False
                x = x+1

        tup = tuple()
        ulist = unique(count)
        tup = key1, ulist
        reduce1.append(tup)
    return reduce1

# tup to dic
def Convert1(tup, di):
    di = dict(tup)
    return di

