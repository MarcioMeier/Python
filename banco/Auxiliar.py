import locale
import datetime
import readline

def inputInt(pergunta):
    pergunta=pergunta+"\n"
    numero = input(pergunta)
    try:
        numero = int(numero)
    except ValueError:
        print('Valor digitado é incorreto! valro digitado (%s)' %(numero))
        return False
    return numero

def inputFloat(pergunta):
    pergunta=pergunta+"\n"
    numero = input(pergunta)
    try:
        numero = float(numero)
    except ValueError:
        print('Valor digitado é incorreto! valro digitado (%s)' %(numero))
        return False
    return numero

def inputDate(pergunta):
    pergunta=pergunta+"\n"
    data = input(pergunta)
    locale.setlocale(locale.LC_TIME, 'pt_BR.utf8')
    try:
        dia,mes,ano = map(int, data.split('/'))
        data1=datetime.date(ano,mes,dia)
    except ValueError:
        print('Valor digitado é incorreto! valor digitado (%s), valor esperado (AAAA/MM/DD)' %(data))
        return False
    return data

def inputSugestao(pergunta, preenchimento=''):
   pergunta=pergunta+"\n"
   readline.set_startup_hook(lambda: readline.insert_text(preenchimento))
   try:
      return input(pergunta)
   finally:
      readline.set_startup_hook()