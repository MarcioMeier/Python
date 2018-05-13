# Marcio e Ronei => Onde vão as maiores despesas (qual tipo Ex: Passagem aérea, Veículos Automotores, Telefone, etc...)
#
#
import csv
import sys
import collections
import locale
from decimal import Decimal
import os
from pathlib import Path
#
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
#
arquivo = open(os.path.dirname(os.path.realpath(__file__))+"/Ano-2017.csv","r",encoding="utf-8")

lista = csv.DictReader(arquivo,delimiter=";")

despesas={}

for linha in lista:

    tipoDespesa = linha['txtDescricao']
    valorDocumento = linha['vlrLiquido']

    valorDocumento=float(valorDocumento.replace(',','.'))
    tipoDespesa = tipoDespesa.lower()

    if tipoDespesa in despesas.keys():
        totalTipoDespesa=despesas[tipoDespesa]
        totalTipoDespesa+=valorDocumento
        despesas[tipoDespesa]=totalTipoDespesa

    else:
        despesas[tipoDespesa]=valorDocumento

arquivo.close()

despesasTotais={}

for key, valorTotal in despesas.items():

    despesasTotais[valorTotal]=key

despesasTotaisOrdenada = collections.OrderedDict(sorted(despesasTotais.items()))



maiorGasto = float(sorted(despesasTotaisOrdenada.keys())[-1])
naturezaMaiorGasto = despesasTotaisOrdenada[maiorGasto]

menorGasto = float(sorted(despesasTotaisOrdenada.keys())[0])
naturezaMenorGasto = despesasTotaisOrdenada[menorGasto]

maiorGasto=locale.currency(maiorGasto, grouping=True, symbol=None)
menorGasto=locale.currency(menorGasto, grouping=True, symbol=None)
print("\n\n\n")
print("A natureza de maior gasto é %s com o gasto de: %s" %(naturezaMaiorGasto,maiorGasto))
print("A natureza de menor gasto é %s com o gasto de: %s\n" %(naturezaMenorGasto, menorGasto))
print("A lista inteira do maior para o menor é:")

for key in range(1,len(despesasTotaisOrdenada)+1):
    i = key*-1
    valor = float(sorted(despesasTotaisOrdenada.keys())[i])
    natureza = despesasTotaisOrdenada[valor]
    valor=locale.currency(valor, grouping=True, symbol=None)
    print("valor: %s natureza: %s " %(valor,natureza))

#