import pandas as pd 
import numpy  as np 
from collections import Counter


def calcMaha(archivo):
    dataFrame = pd.read_excel(archivo)
    print(dataFrame)
    filas, col = dataFrame.shape
    print("Numero de columnas: ", filas)
    cent, listCent = centOp(dataFrame,filas)
    matrizDf, df_df = opDF(dataFrame,cent,filas)
    distsM(dataFrame,filas,matrizDf,listCent)

def centOp(dataFrame,filas):
    listMatriz = []
    listCent = []

    for k in dataFrame:
        centroide = 0
        centroide = dataFrame[k].sum()
        centroide = centroide / filas
        listCent.append(centroide)
    print(listCent)
    
    for i in range(filas):
        listMatriz.append(listCent)
    print(listMatriz)
    df2 = pd.DataFrame(listMatriz)
    print("Array generado:")
    print(df2)
    
    return df2,listCent

def opDF(df1,df2,filas):
    print("*___________________________________________________________________________________________")
    matriz1 = []
    matriz2 = []
    matriz1 = df1.values
    matriz2 = df2.values
    
    A = ((np.transpose(matriz1 - matriz2)))
    B = (matriz1 - matriz2)
    f = np.dot(A,B)
    f = np.divide(f, filas-1)
    f2 = pd.DataFrame(f)
    print(f2)
    
    return f,f2

def distsM(df, filas,matrizDf,listCent):
    print("*___________________________________________________________________________________________")
    matriz1 = df.values
    matriz2 = matriz1
    cont = 1
    listAux = []
    flag = False
    mFinal = []
    
    for i in matriz1:
        print("List Num: ", cont, i)
        listAux = i
        flag3 = False
        
        for j in matriz2:
            flag = Counter (i) == Counter(j)
            flag2 = (Counter (listAux) == Counter(j))
            
            if((len(i) != 0) and flag == False and flag3):
                print("La resta de ", i, " y " , j)
                rest = (i - j)
                inversa = np.linalg.inv(matrizDf)
                transpose = ((np.transpose(rest)))
                mult = np.dot(inversa,transpose)
                dis = np.dot(rest,mult)
                print(dis)
                listSave.append(dis)
                
            elif(flag2 == True):
                rest = listAux-listCent
                inversa = np.linalg.inv(matrizDf)
                transpose = ((np.transpose(rest)))
                mult = np.dot(inversa,transpose)
                dist = np.dot(rest,mult)
                listSave = []
                print("La diagonal queda de la siguiente manera: ", dist)
                listSave.append(dist)
                flag3 = True
                
        while len(listSave) < filas:
            listSave.insert(0, 0)
        mFinal.append(listSave)
        cont = 1 + cont
    df_final = pd.DataFrame(mFinal)
    print("*___________________________________________________________________________________________")
    print(df_final)
archivo = ("C:/Users/juanj/OneDrive/Documentos/UAMExISI/Rodo/prueba1.xlsx")
result  = calcMaha(archivo)