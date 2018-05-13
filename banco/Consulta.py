import DAO
import Auxiliar
import os
import csv
import collections
import locale
from decimal import Decimal

def obterSaldoAtual():
    transacao = DAO.recuperar("transacao.csv")
    saldo=0
    primeiraLinha=True
    for i in transacao:
        if primeiraLinha:
            primeiraLinha=False
            continue
        #
        valor=float(i[2])
        natureza=i[4]
        #
        if ( natureza.lower() == "saida" ):
            saldo-=valor
        elif ( natureza.lower() == "entrada" ):
            saldo+=valor
    #
    return saldo

def extrato():
    caminhoSugestao=os.path.dirname(os.path.realpath(__file__))

    while True:
        localArquivo = Auxiliar.inputSugestao("Escolha o local que será salvado arquivo:",caminhoSugestao)
        if (os.path.isdir(localArquivo)):
            break
        else:
            print("Caminho não encontrado!\n")
    #
    if localArquivo[-1:]!="/":
        localArquivo=localArquivo+"/"

    lista = DAO.recuperar("transacao.csv")
    # data;lancamento;valor;tipoTransacao;natureza
    primeiraLinha = True
    dados={}
    for item in lista:
        if primeiraLinha:
            primeiraLinha=False
            continue
        #
        data = item[0]
        descLancamento = item[1]
        valor = float(item[2])
        natureza = item[4]
        lista = [descLancamento,valor,natureza]
        if data in dados:
            index=len(dados[data])
            dados[data][index]=lista
        else:
            dados[data]={}
            dados[data][0]=lista

    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
    caminhoArquivo=localArquivo+"extrato.csv"
    cabecalho=["Data","Lançamento","Valor(R$)","Saldo(R$)"]
    
    with open(caminhoArquivo, 'w', newline='') as arquivoCSV:
        escreverCSV = csv.DictWriter(arquivoCSV, delimiter=";", fieldnames=cabecalho)
        escreverCSV.writeheader()
        
        saldo=0
        for key in sorted(dados):
            for x in range(1,len(dados[key])+1):
                itens = dados[key][x-1]
                #
                descLancamento = itens[0]
                valor = float(itens[1])
                natureza = itens[2]
                #
                operacao=""
                if natureza.lower()=="saida":
                    operacao="-"
                #
                valorDesc=operacao+str(locale.currency(valor, grouping=True, symbol=None))
                
                if natureza.lower()=="saida":
                    saldo-=valor
                else:
                    saldo+=valor
                
                linha={"Data":key,"Lançamento":descLancamento,"Valor(R$)":valorDesc,"Saldo(R$)":""}
                escreverCSV.writerow(linha)
            
            sadoDesc=locale.currency(saldo, grouping=True, symbol=None)
            saldoDia={"Data":key,"Lançamento":"SALDO CONTA CORRENTE","Valor(R$)":"","Saldo(R$)":sadoDesc}
            escreverCSV.writerow(saldoDia)
    return caminhoArquivo

                
                