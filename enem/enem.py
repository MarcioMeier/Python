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
        # grava dicionario de nota com a chave como número da inscrição
        notas[numeroInscricao]=notaFinal
        #
        # grava dicionario de idade do candidato com a chave como número da inscrição (creitério de desempate de nota é a idade)
        candidato[numeroInscricao]=idadeCandidato

# ordena pelo valor (no caso: nota)
notasOrdenadas=sorted(notas, key=notas.__getitem__)
notasFinais={}

sair=False
contador=len(notasOrdenadas)
# itera as 50 melhores notas (margem para notas iguais, desempate:idade)
for key in range(contador,contador-50,-1):
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
    # Lê todos as notas já colocadas
    for chave,valor in notasFinais.items():
        # se a nota do candidato atual (loop anterior) for maior ou igual a de uma ja listada:
        if notaFinal>=valor:
            idadeCandidatoA=candidato[chave]
            #
            # se a idade do candidato atual for maior do que o da nota ja listada:
            if idadeCandidato>idadeCandidatoA:
                #
                # se o candidato atual não tiver na lista ainda:
                if numeroInscricao not in lista:
                    lista.append(numeroInscricao)
        lista.append(chave)
        #
        # se a lista ja tiver mais de 20 notas e a nota atual for menor que a 20ª:
        if len(lista)>20:
            if lista.index(19)>notas[chave]:
                sair=True
    notasFinais={}
    #
    # itera a lista criada anteriormente e recria o dicionario das 20 melhores notas
    for x in lista:
        notasFinais[x]=float(format(notas[x],'.2f'))
        if len(notasFinais)==20:
            break
    #
    # se o candidato atual não estiver no dicionario recém criado significa que ele tirou uma nota inferior a todas as outras
    # ou tirou a mesma nota mas tem uma idade inferior aos outros candidatos
    if numeroInscricao not in notasFinais:
        notasFinais[numeroInscricao]=notaFinal
    #
    # se já tiver as 20 melhores notas e a nota atual for menor que a 20º encerra o loop
    if sair:
        break
#
# monta o JSON para resposta
respostaFinal={}
respostaFinal["token"]="Márcio Meier"
respostaFinal["email"]="marcio_meier@estudante.sc.senai.br"
values = [{"NU_INSCRICAO": k,"NOTA_FINAL":v} for k,v in notasFinais.items()]
respostaFinal["answer"]=values
#
#print(respostaFinal)
print(json.dumps(respostaFinal, indent=4))