import pandas as pd
import numpy as np


def centroide(df, rows):
    cent = []
    for index in range(df.shape[1]):
        sum = 0
        col_val = df.iloc[: , index].values
        for val in col_val:
            sum += val
        sum = sum / rows
        cent.append(sum)
    print(cent, "\n")
    return cent


def n_x(cent, rows):
    m_new = []
    for i in range(0, rows):
        m_new.append(cent)

    nue_df = pd.DataFrame(m_new)
    print(nue_df, "\n")
    return nue_df


def mult(x1, x1_t):
    x1 = x1.to_numpy()
    x1_t = x1_t.to_numpy()
    res = np.dot(x1_t, x1)
    res = pd.DataFrame(res)
    print(res, "\n")
    return res

def dis_square(df, df_cov, rows):
    resul = {}
    for index in range(df.shape[0]):
        row_val = df.iloc[index].values
        for i in range(index + 1, rows):
            r_val = df.iloc[i].values
            res = row_val - r_val
            res_val =np.dot(res, df_cov)
            res_val =np.dot(res_val, res.T)
            print(f"d2(X{index+1}, X{i+1}) = {res_val}")
            resul[f"{index},{i}"] = res_val
    print("\n")
    return resul
        
def diagonal(df, centroide, matriz_cov):
    diagonal = []
    for index in range(df.shape[0]):
        resta = None
        row_val = df.iloc[index].values
        resta = row_val - centroide
        mult = np.dot(resta, matriz_cov)
        mult = np.dot(mult, resta.T)
        diagonal.append(mult)
        print(f"d2m(X{index+1} - n) = {mult}")
    print("\n")
    return diagonal

def matriz_fin(df, res):
    for index in range(df.shape[0]):
        row_val = df.iloc[index].values
        for i in range(0, len(row_val)):
            if df[index][i] == 0.0:
                pos = f"{index},{i}"
                df[index][i] = res[pos] if pos in res else 0.0
    print(df)


df = pd.read_excel("D:/Archivos 9no Semestre/Docs Finales/UAMExISI/Rodo/prueba1.xlsx",  header=None)
print(df, "\n")

filas = len(df.axes[0])
print(filas, "\n")

cent = centroide(df, filas)

x_f = n_x(cent, filas)

x2 = df - x_f
print(x2, "\n")

x2_T = x2.T
print(x2_T, "\n")

df_mult = mult(x2, x2_T)

cov = (filas -1) / 1
print(cov, "\n")

df_cov = df_mult / cov
print(df_cov, "\n")

df_cov_inv = np.array(df_cov)
df_cov_inv = np.linalg.inv(df_cov)
print(df_cov_inv, "\n")

d_cuadradas = dis_square(df, df_cov_inv, filas)

diagonal = diagonal(df, cent, df_cov_inv)

m_fin = np.diagflat(diagonal)
m_fin = pd.DataFrame(m_fin)
matriz_fin(m_fin, d_cuadradas)