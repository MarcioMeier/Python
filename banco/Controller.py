import Transacao
import DAO
import Menu
import Consulta
import os
import sys
import subprocess

def lancamento():
  menu = Menu.menuLancamento()
  #
  codOpcao = menu["opcao"]
  descOpcao = menu["menu"][codOpcao]
  #
  if ( descOpcao.lower() == "débito" ):
    transacao = Transacao.proxyDebito()
    if transacao:
      print("Lançamento realizado com sucesso!")
    else:
      print("Houve um erro no lançamento!")
  #
  elif ( descOpcao.lower() == "crédito" ):
    opcao = Menu.menuCredito()
    tipoTransacao = opcao["menu"][opcao["opcao"]]
    transacao = Transacao.proxyCredito(tipoTransacao)
    if transacao:
      print("Lançamento realizado com sucesso!")
    else:
      print("Houve um erro no lançamento!")
  
def consultarSaldo():
  saldo = Consulta.obterSaldoAtual()

  if (saldo  < 0):
    print("Você está devendo %2.f para o banco!" %(saldo*-1))
  else:
    print("Seu saldo é: %2.f" %(saldo))
  
def consultarExtrato():
  caminho = Consulta.extrato()
  print("Arquivo gerado em:",caminho)
  opener ="open" if sys.platform == "darwin" else "xdg-open"
  subprocess.call([opener, caminho])
