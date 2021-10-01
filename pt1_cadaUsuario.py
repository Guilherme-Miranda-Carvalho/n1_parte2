listaUsuario = []   #lista cadastro usuário
novoUsuario = {}    #dicionario cadastro usuário
testCad = 1         #variavel teste para novo usuário
nomeCriarUsuario = "" #variavel cadastro usuário
emailCriarUsuario = ""   #variavel cadastro usuário

# inicio menu
def menu():
    num = int
    print("\n-------------Menu-------------")
    print("\nDigite um numero correspondente ao menu: \n[1] - Cadastrar novo usuário \n[2] - Exibir todos usuários por ordem de cadastro \n[3] - Exibir todos usuários por ordem alfabética \n[4] - Buscar usuário \n[5] - Remover um usuário \n[6] - Alterar um usuário")
    num = int(input())
    if (num == 1):
        criarUsuario()
    elif (num == 2):
        pass
    elif (num == 3):
        pass
    elif (num == 4):
        pass
    elif (num == 5):
        pass
    elif (num == 6):
        pass
    else:
        print("Numero digitado não corresponde as opções do menu, digite um numero valido!")
# fim  menu

# inicio cadastro usuário
def criarUsuario():
    print("\n-------------Novo Usuário-------------")
    novoUsuario["nome"] = input("\nDigite o nome completo do usuário: ")
    novoUsuario["email"] = input("Digite o e-mail do usuário: ")
    listaUsuario.append(novoUsuario)
    testCriarUsuario()
    return novoUsuario
# fim cadastro usuário

# inicio teste usuário

# fim teste usuário  


# inicio teste para novo usuário
def testCriarUsuario():
    print("\nDeseja cadastrar outro usuário?\n[1]Sim\n[2]Não")
    testCad = int(input())
    if (testCad == 1):
        criarUsuario()
    elif (testCad == 2):
        menu()
    else:
        print("\nDigite um numero valido para essa operação")
        testCriarUsuario()
# fim teste para novo usuário

if __name__ == "__main__":
    menu()
