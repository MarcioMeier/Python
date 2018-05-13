#
import csv
import sys
import os
from pathlib import Path
#
arquivo = open(os.path.dirname(os.path.realpath(__file__))+"/salariosSC.csv","r",encoding = "ISO-8859-1")

lista = csv.DictReader(arquivo,delimiter=";")

salarioSTF = 33763

salarioTeto = salarioSTF * 0.9

listaAcimaTeto=[]

arquivo2 = open(os.path.dirname(os.path.realpath(__file__))+"/salariosAcimaTeto.csv","w",encoding = "ISO-8859-1")

fieldnames = ['Nome', 'CPF', 'ValorBruto', 'Cargo', 'OrgaoExercicio', 'OrgaoOrigem']

escreverCSV = csv.DictWriter(arquivo2, delimiter=';', fieldnames=fieldnames)

escreverCSV.writeheader()
contador=0

for linha in lista:
    # desvia a primeira linha
    if (linha['Nome']=="Nome"):
        continue
    #
    # obtém os valores das colunas para cada linha
    nome = linha['Nome']
    cpf = linha['CPF']
    valorBruto = linha['ValorBruto']
    cargo = linha['Cargo']
    orgaoExercicio = linha['OrgaoExercicio']
    orgaoOrigem = linha['OrgaoOrigem']
    #
    if (float(valorBruto) > float(salarioTeto)):
        contador=contador+1

        escreverCSV.writerow({'Nome': nome, 'CPF': cpf,'ValorBruto': valorBruto,'Cargo': cargo,'OrgaoExercicio': orgaoExercicio,'OrgaoOrigem': orgaoOrigem})

print('\n\nHá %i servidores públicos com salário acima do teto!' %(contador))

arquivo.close()
arquivo2.close()
