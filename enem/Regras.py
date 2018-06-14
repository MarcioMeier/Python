def ProvaValida(dados):
        #
        if int(dados['TP_PRESENCA_CN'])!=1: return False    # Sem presença na prova de Ciências da Natureza ou prova anulada
        if int(dados['TP_PRESENCA_CH'])!=1: return False    # Sem presença na prova de Ciências Humanas ou prova anulada
        if int(dados['TP_PRESENCA_LC'])!=1: return False    # Sem presença na prova de Linguagens e Códigos ou prova anulada
        if int(dados['TP_PRESENCA_MT'])!=1: return False    # Sem presença na prova de Matemática ou prova anulada
        if int(dados['TP_STATUS_REDACAO'])>1: return False  # Redação com problemas, anulada
        #    
        return True
        
def ObterNotaFinal(dados):

    listaProvas=['CN','CH','LC','MT','REDACAO']
    pesos={
        "MT":3,
        "CN":2,
        "LC":1.5,
        "CH":1,
        "REDACAO":3
    }

    notas={}
    for i in listaProvas:
        notaProva=dados['NU_NOTA_'+i]
        notaProva=float(notaProva.replace(',','.'))
        notas[i]=notaProva*pesos[i]
    
    notaFinal=0
    for nota in notas.values():
        notaFinal+=float(nota)

    notaFinal=notaFinal/5
    return notaFinal
#