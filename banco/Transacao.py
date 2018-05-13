import Auxiliar
import DAO
import csv

def debito(data,lancamento,valor):
    #data=False
    while not data:
        data = Auxiliar.inputDate("Digite a data da transação:")
    #valor=False
    while not valor:
        valor = Auxiliar.inputFloat("Digite o valor da transação:")
    #lancamento=False
    while not lancamento:
        lancamento = input("Digite uma descrição para o lançamento:\n")
    
    return DAO.inserirLancamento(data,lancamento,valor,"dinheiro","saida")

def credito(data,lancamento,valor,tipo):
    #data=False
    while not data:
        data = Auxiliar.inputDate("Digite a data da transação:")
    #valor=False
    while not valor:
        valor = Auxiliar.inputFloat("Digite o valor da transação:")
    #lancamento=False
    while not lancamento:
        lancamento = input("Digite uma descrição para o lançamento:\n")
    
    return DAO.inserirLancamento(data,lancamento,valor,tipo,"entrada")


def proxyDebito():
    return debito("","","")

def proxyCredito(tipo):
    return credito("","","",tipo)