listaUsuario = []   #lista cadastro usuário
testCad = 1         #variavel teste para novo usuário

# inicio menu
def menu():
    print("\n-------------Menu-------------")
    print("\nDigite um numero correspondente ao menu: \n[1] - Cadastrar novo usuário \n[2] - Exibir todos usuários por ordem de cadastro \n[3] - Exibir todos usuários por ordem alfabética \n[4] - Buscar usuário \n[5] - Remover um usuário \n[6] - Alterar um usuário")
    num = input()
    if (num == '1'):
        criarUsuario()
    elif (num == '2'):
        exibirUsuario()
    elif (num == '3'):
        pass
    elif (num == '4'):
        pass
    elif (num == '5'):
        pass
    elif (num == '6'):
        pass
    else:
        print("Numero digitado não corresponde as opções do menu, digite um numero valido!")
        menu()
# fim  menu

# inicio cadastro usuário
def criarUsuario():
    print("\n-------------Novo Usuário-------------")
    novoUsuario = {}
    nomeCriarUsuario = input("\nDigite o nome completo do usuário: ")
    emailCriarUsuario = input("Digite o e-mail do usuário: ")
    if(nomeCriarUsuario == "" or emailCriarUsuario == ""):
        print("\n-------------Preencha todos os campos!-------------")
        criarUsuario()
    else:
        testNovoCad = testeUsuarioExistente(nomeCriarUsuario, emailCriarUsuario)
        if (True == testNovoCad):
            novoUsuario["nome"] = nomeCriarUsuario
            novoUsuario["email"] = emailCriarUsuario
            listaUsuario.append(novoUsuario)
            print("\n-------------Usuário cadastrado com sucesso!-------------")
        testCriarUsuario()

    return novoUsuario
# fim cadastro usuário

# inicio teste usuário
def testeUsuarioExistente(nome = str, email = str):
    testNovo = True
    if(len(listaUsuario) != 0):
        i = 0
        while i < len(listaUsuario):
            if(listaUsuario[i]['nome'].upper() == nome.upper()):
                print("\n-------------Usuário já existe, digite um nome diferente-------------")
                testNovo = False 
            if (listaUsuario[i]['email'].upper() == email.upper()):
                print("\n-------------Usuário já existe, digite um email diferente-------------")
                testNovo = False                   
            i = i+1
    return testNovo
# fim teste usuário  


# inicio teste para novo usuário
def testCriarUsuario():
    print("\nDeseja cadastrar outro usuário?\n[1]Sim\n[2]Não")
    testCad = input()
    if (testCad == '1'):
        criarUsuario()
    elif (testCad == '2'):
        menu()
    else:
        print("\n-------------Digite um numero valido para essa operação-------------")
        testCriarUsuario()
# fim teste para novo usuário

# inicio exibir usuário por ordem de cadastro
def exibirUsuario():
    if(len(listaUsuario) != 0):
        i = 0
        print("\n-------------Usuários cadastrados-------------")
        while i < len(listaUsuario):   
            if(i == 0):
                print("\nNome: ",listaUsuario[i]['nome'],"\nE-mail: ",listaUsuario[i]['email'])
                i = i+1
            elif(i != 0):
                print("\n----------------------------------------------")
                print("\nNome: ",listaUsuario[i]['nome'],"\nE-mail: ",listaUsuario[i]['email'])
                i = i+1
        menu()
    else:
        print("\n-------------Nenhum usuário cadastrado-------------")
        menu()
#fim exibir usuário por ordem de cadastro

if __name__ == "__main__":
    menu()