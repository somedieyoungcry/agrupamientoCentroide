#from multiprocessing.resource_sharer import stop
#from tracemalloc import start
import pandas as pd 
#import numpy  as np 
from scipy.spatial import distance_matrix
from scipy.stats import zscore

def evalAmb(df):
    print("~~~~~~~~~~~~~~~~~~~~Evaluamos ambito UwUr~~~~~~~~~~~~~~~~~")
    dec = False
    cen = False
    mil = False#

    for key in df:
        for val in df[key]:
            if val in range(0, 99):
                dec = True
            if val in range(100, 999):
                cen = True
            if val in range(1000, 9999):
                mil = True

    if dec and cen:
        return True
    elif dec and mil:
        return True
    elif cen and mil:
        return True
    else:
        return False

rut = ("Rodo/Libro1.csv")
df = pd.read_excel(rut , sheet_name = "Hoja1")
print(df)
list = []
filas, columnas = df.shape

if(filas <= 256 and columnas <= 30):
    print("Pass")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    ambito = evalAmb(df)
    if(ambito == True):
        print("Obtenemos puntuacion Z")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        datos = df.values
        pZ = zscore(datos)
        re = pd.DataFrame(distance_matrix(pZ, pZ, p=2))
        print(re)
    else:
        #ojo distancia
        re = pd.DataFrame(distance_matrix(df.values, df.values), index=df.index, columns=df.index)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Euclidiana: \n", re)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
else:
    print("error")
    print("Registro supera a 256: ", filas)
    print("Registro supera a 30: ", columnas)

