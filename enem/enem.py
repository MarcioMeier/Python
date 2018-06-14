import csv
import Regras
import os
import json

cwd = os.getcwd()

arquivo=cwd+"\\enem\\train.csv"


notas={}
candidato={}

print("Processando dados...\n")

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
notasFinais={}

sair=False
contador=len(notasOrdenadas)
for key in range(contador,contador-20,-1):
    #
    numeroInscricao=notasOrdenadas[key-1]
    #
    notaFinal = notas[numeroInscricao]
    idadeCandidato=candidato[numeroInscricao]
    #
    if numeroInscricao in notasFinais:
        continue
    #
    lista=[]
    for chave,valor in notasFinais.items():
        if notaFinal>=valor:
            idadeCandidatoA=candidato[chave]
            if idadeCandidato>idadeCandidatoA:
                if numeroInscricao not in lsita:
                    lista.append(numeroInscricao)
        lista.append(chave)
        if len(lista)>20 and lista.index(19)>notas[chave]:
            sair=True
    notasFinais={}
    for x in lista:
        notasFinais[x]=float(format(notas[x],'.2f'))
        if len(notasFinais)==20:
            break
    #
    if numeroInscricao not in notasFinais:
        notasFinais[numeroInscricao]=notaFinal
    #
    if sair:
        break

respostaFinal={}
respostaFinal["token"]="Márcio Meier"
respostaFinal["email"]="marcio_meier@estudante.sc.senai.br"
values = [{"NU_INSCRICAO": k,"NOTA_FINAL":v} for k,v in notasFinais.items()]
respostaFinal["answer"]=values
#
#print(respostaFinal)
print(json.dumps(respostaFinal, indent=4))