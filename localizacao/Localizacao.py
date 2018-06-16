import pandas as pd
import numpy as np
import os

cwd = os.getcwd()
arquivo=cwd+"\\localizacao\\escolasJgs.csv"

tamanhoBloco = 1e3
i=1
dados=0
colunas = ["Escola","Endereco","Bairro","Tipo"]

for pedaco in pd.read_csv(arquivo, chunksize=tamanhoBloco, index_col=None, encoding="latin-1", usecols=colunas, delimiter=","):
    linha=pedaco.dropna(subset=colunas)
    print(linha)