import Menu
import Controller
import sys

while True:
    menu = Menu.menuPrincipal()
    #
    # obter código da opção = menu["opcao"]
    # obter descrição da opção = menu["menu"][menu["opcao"]]
    #
    codOpcao = menu["opcao"]
    descOpcao = menu["menu"][codOpcao]
    #
    if ( descOpcao.lower() == "lançamento" ):
        Controller.lancamento()

    elif ( descOpcao.lower() == "consultar saldo" ):
        Controller.consultarSaldo()

    elif ( descOpcao.lower() == "consultar extrato" ):
        Controller.consultarExtrato()

    elif ( descOpcao.lower() == "sair" ):
        sys.exit("Bye bye :)")