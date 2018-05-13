def listaMenu(menu):
  for x in menu:
    print ("para", x + ", digite" , "[" + str(menu.index(x)) + "]")

def ObterOpcao(menu):
  while True:
    opcao=input("\nDigite a opção: ")
    try:
      if opcao in menu:
        opcaoString = opcao
        opcao = menu.index(opcaoString)
        break
      opcao = int(opcao)
      opcaoString=menu[opcao]
      if opcaoString:
        break
    except ValueError:
      print ("Opção Inválida\n")

  print("opcao {}: {}".format(opcao,opcaoString))
  return opcao

def menuPrincipal():
  menu=["Lançamento","Consultar Saldo","Consultar Extrato","Sair"]
  print("\n\n**** Menu: ****")
  listaMenu(menu)
  return {"opcao":ObterOpcao(menu),"menu":menu}

def menuLancamento():
  menu=["Débito","Crédito"]
  print("**** Fazer Lançamento: ****")
  listaMenu(menu)
  return {"opcao":ObterOpcao(menu),"menu":menu}

def menuCredito():
    menu=["Dinheiro","Cheque"]
    print("**** Tipo de Entrada: ****")
    listaMenu(menu)
    return {"opcao":ObterOpcao(menu),"menu":menu}