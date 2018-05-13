import os
import csv
from pathlib import Path
#
#
def obterCaminhoArquivo(nomeArquivo):
    return os.path.dirname(os.path.realpath(__file__))+"/"+nomeArquivo
#
#
def verificarArquivoExistente(nomeArquivo):
    return os.path.isfile(obterCaminhoArquivo(nomeArquivo))
#
#
def criarArquivo(nomeArquivo,delimitador,cabecalho):
    caminhoArquivo = obterCaminhoArquivo(nomeArquivo)
    with open(caminhoArquivo, 'w', newline='') as arquivoCSV:
        writer = csv.DictWriter(arquivoCSV, delimiter=delimitador, fieldnames=cabecalho)
        writer.writeheader()
    return verificarArquivoExistente(nomeArquivo)
#
#
def salvar(nomeArquivo,delimitador,dados,cabecalho):
    caminhoArquivo = obterCaminhoArquivo(nomeArquivo)
    #
    if not verificarArquivoExistente(nomeArquivo):
        criou=False
        while not criou:
            criou = criarArquivo(nomeArquivo,delimitador,cabecalho)
    #
    lista=recuperar(nomeArquivo)
    lista.append(dados)
    #
    with open(caminhoArquivo, 'w', newline='') as arquivoCSV:
        escreverCSV = csv.writer(arquivoCSV, delimiter=';')
        for i in lista:
            escreverCSV.writerow(i)
    return True
#
#
def recuperar(nomeArquivo):
    if not verificarArquivoExistente(nomeArquivo):
        return []
    caminhoArquivo = obterCaminhoArquivo(nomeArquivo)
    lista=[]
    with open(caminhoArquivo, newline='') as arquivoCSV:
        spamreader = csv.reader(arquivoCSV, delimiter=';')
        for row in spamreader:
            lista.append(row)
    return lista
#
#
def inserirLancamento(data,lancamento,valor,tipoTransacao,natureza):
    dados = [data,lancamento,valor,tipoTransacao,natureza]
    nomeArquivo="/transacao.csv"
    cabecalho=["data","lancamento","valor","tipoTransacao","natureza"]
    return salvar(nomeArquivo,";",dados,cabecalho)