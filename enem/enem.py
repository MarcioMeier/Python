import csv
import Regras


arquivo="C:\\Users\\Aluno\\Desktop\\train.csv"


notas={}
candidato={}

with open(arquivo, newline='', encoding='utf-8') as dadosEnem:
    #
    leitor = csv.DictReader(dadosEnem, delimiter=",")
    for linha in leitor:
        #
        if Regras.ProvaValida(linha)==False: continue
        #
        numeroInscricao=linha['NU_INSCRICAO']
        idadeCandidato=linha['NU_IDADE']
        #
        notaFinal=Regras.ObterNotaFinal(linha)
        #
        notas[numeroInscricao]=notaFinal
        candidato[numeroInscricao]=idadeCandidato


notasOrdenadas=sorted(notas, key=notas.__getitem__)

for key,value in notasOrdenadas:
    
