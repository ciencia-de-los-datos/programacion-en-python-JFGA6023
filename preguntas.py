"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""



def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/p
    214
     """
    data = open('data.csv','r').readlines()
    col2 = [int(row[2]) for row in data]
    suma = sum(col2)
    print(suma)
    return suma  
    
pregunta_01()

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
    data = open('data.csv','r').readlines()
    col0 = [(row[0]) for row in data]
    list_l=[]
    for element in col0:
        if element not in list_l:
         list_l.append(element)
        else:
         continue
    
    list_l.sort()

    list_count=[]
    for element in list_l:
        list_count.append(col0.count(element))
    
    list_count
    List=list(zip(list_l,list_count))
    print ( List)

    return List

pregunta_02()

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

    data = open('data.csv','r').readlines()
    col0 = [(row[0]) for row in data]
    list_l=[]
    for element in col0:
        if element not in list_l:
         list_l.append(element)
        else:
         continue
    list_l.sort()
    suma=[]
    e=[]
    c=0
    for element in list_l:
       for i in data:
          if i[0] == list_l[c]:
             e.append(int(i[2]))

          else:
              continue   
       suma.append(sum(e))      
       c+=1
       e=[]
    List=list(zip(list_l,suma))  
    print(List)

    return List

pregunta_03()

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
    data = open('data.csv','r').readlines()
    data=[f.replace('\n','') for f in data]
    data=[f.split('\t') for f in data]
    col3=[i[2].split('-') for i in data]
    list_months=[i[1]for i in col3]
    months=sorted(set([i for i in list_months]))
    tuple_date_counts=[(x,list_months.count(x)) for x in months] 
    print(tuple_date_counts)
    return
    
pregunta_04()

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
    data = open('data.csv','r').readlines()
    col0 = [(row[0]) for row in data]
    list_l=[]
    for element in col0:
        if element not in list_l:
         list_l.append(element)
        else:
         continue
    list_l.sort()
    minimo=[]
    maximo=[]
    e=[]
    c=0
    for element in list_l:
       for i in data:
          if i[0] == list_l[c]:
             e.append(int(i[2]))

          else:
              continue   
       minimo.append(min(e))  
       maximo.append(max(e))    
       c+=1
       e=[]
    List=list(zip(list_l,maximo,minimo))  
    print(List)

    return
pregunta_05()

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

    with open('data.csv','r') as file:
       data=file.readlines()
    data=[row.replace("\n","") for row in data]
    data=[row.split("\t") for row in data]
    col4=[col[4].split(',') for col in data]
    list_key_value = [ (y[:3],int(y[4:])) for x in col4 for y in x ]
    keys=sorted(set(i[0] for i in list_key_value))
    valores=[]
    tuplas=[]
    for key in keys:
        for i in list_key_value:
            if i[0]==key:
                valores.append(i[1])
        tuplas.append((key, min(valores), max(valores)))
        valores.clear()
    print(tuplas)
    return tuplas    

pregunta_06()

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
    data = open('data.csv','r').readlines()
    col1 = [(row[2]) for row in data]
    list_l=[]
    list_letters=[]
    for element in col1:
        if element not in list_l:
         list_l.append(element)
        else:
         continue
    list_l.sort()
    List=[]
    
    e=[]
    c=0
    for element in list_l:
       for i in data:
          if i[2] == list_l[c]:
              e.append(i[0])
              
          else:
              continue   
       
       list_letters=e
       Listi=(c,list_letters)
       List.append(Listi)
       
       e=[]
       c+=1
    print(List)  
    return List
pregunta_07()

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
    data = open('data.csv','r').readlines()
    col1 = [(row[2]) for row in data]
    list_l=[]
    list_letters=[]
    for element in col1:
        if element not in list_l:
         list_l.append(element)
        else:
         continue
    list_l.sort()
    List=[]
    
    e=[]
    c=0
    for element in list_l:
       for i in data:
          if i[2] == list_l[c]:
              e.append(i[0])
              
          else:
              continue   
       
       list_letters=e
       list_letters=list(set(list_letters))
       list_letters.sort()
       Listi=(c,list_letters)
       List.append(Listi)
       
       e=[]
       c+=1
    print(List)  
    return List
pregunta_08()


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
    data = open('data.csv','r').readlines()
    data=[i.replace('\n','') for i in data]
    data=[i.split('\t') for i in data]
    col5=[i[4].split(',') for i in data]

    list_keys=[(i[:3]) for x in col5 for i in x]
    keys=sorted(set(i for i in list_keys))
    tuple_key_counts=[(i,list_keys.count(i)) for i in keys]
    dict_key_counts=dict(tuple_key_counts)
    print(dict_key_counts)
    return dict_key_counts

pregunta_09()
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
    data = open('data.csv','r').readlines()
    data=[i.replace('\n','') for i in data]
    data=[i.split('\t') for i in data]
    col4=[len(i[3].split(',')) for i in data]
    col5=[len(i[4].split(',')) for i in data]
    col1=[(i[0]) for i in data]
    List_tuples=list(zip(col1,col4,col5))
    print(List_tuples)

    return List_tuples
pregunta_10()

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
    data = open('data.csv','r').readlines()
    data=[i.replace('\n','') for i in data]
    data=[i.split('\t') for i in data]
    col2=[int(i[1]) for i in data]
    col4=[(i[3].split(',')) for i in data]
    datos=list(zip(col4,col2))
    print(datos)
    keys=[]
    for x in col4: 
        keys.extend(x)
    print(keys)
    keys_dic=sorted(set(keys))
    
    dic={}
    for key in keys_dic:
        dic[key]=0
    print(dic)

    for x,y in datos:
        for i in x:
            dic[i]+=int(y)

    print(dic)
    return dic
pregunta_11()


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

    data = open('data.csv','r').readlines()
    data=[i.replace('\n','') for i in data]
    data=[i.split('\t') for i in data]
    col1=[(i[0]) for i in data]
    col5=[(i[4].split(',')) for i in data]
    datos=list(zip(col1,col5))

    keys_dic=sorted(set(col1))

    dic={}
    for key in keys_dic:
        dic[key]=0
    
    for x,y in datos:
        for i in y:
            dic[x]+=int(i[4:])

    print(dic)
    return dic
pregunta_12()