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
        exibirUsuarioAlfabetica()
    elif (num == '4'):
        buscarUsuario()
    elif (num == '5'):
        removerUsuario()
    elif (num == '6'):
        alterarUsuario()
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
        print("\n-------------Erro, preencha todos os campos!-------------")
        menu()
    else:
        testNovoCad = testeUsuarioExistente(nomeCriarUsuario, emailCriarUsuario)
        if (True == testNovoCad):
            novoUsuario["nome"] = nomeCriarUsuario.upper()
            novoUsuario["email"] = emailCriarUsuario.upper()
            listaUsuario.append(novoUsuario)
            print("\n-------------Usuário cadastrado com sucesso!-------------")
        menu()
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

# inicio exibir usuário por ordem alfabetica
def exibirUsuarioAlfabetica():
    listaNome = []
    if(len(listaUsuario) != 0):
        i = 0
        while i < len(listaUsuario):   
                listaNome.append(listaUsuario[i]['nome'])
                i = i+1
        listaNome.sort()
        print("\n-------------Usuários cadastrados, listado por nome em ordem alfabetica-------------")

        i2 = 0
        for item2 in listaNome:
            for item in listaUsuario:
                if listaUsuario[listaUsuario.index(item)]['nome'] == item2:
                    if (listaNome.index(item2)== 0):
                        print("\nNome: ",listaUsuario[listaUsuario.index(item)]['nome'],"\nE-mail: ",listaUsuario[listaUsuario.index(item)]['email'])
                    elif (listaNome.index(item2)!= 0):
                        print("\n----------------------------------------------")
                        print("\nNome: ",listaUsuario[listaUsuario.index(item)]['nome'],"\nE-mail: ",listaUsuario[listaUsuario.index(item)]['email'])
        menu()
    else:
        print("\n-------------Nenhum usuário cadastrado-------------")
        menu()
#fim exibir usuário por ordem alfabetica

#inicio buscar usuario
def buscarUsuario():
    if(len(listaUsuario) != 0):
        print("\n-------------Busar usuário cadastrado-------------")
        nomeUsuarioCadastrado = input("\nDigite o nome completo do usuário cadastrado: ")
        verificarUsuarioExiste = False
        if nomeUsuarioCadastrado != "":
            i = 0
            while i < len(listaUsuario):
                if(listaUsuario[i]['nome'].upper() == nomeUsuarioCadastrado.upper()):
                    print("\n-------------Usuário encontrado-------------")
                    print("\nNome: ", listaUsuario[i]['nome'], "\nE-mail:", listaUsuario[i]['email'])
                    verificarUsuarioExiste = True
                i= i+1
            if(verificarUsuarioExiste == False):
                print("\n-------------Usuário não cadastrado-------------")
        else:
            print("\n-------------Erro, preencha todos os campos!-------------")
            menu()
    else:
        print("\n-------------Nenhum usuário cadastrado-------------")
    menu()
#fim buscar usuario

#inicio remover usuario
def removerUsuario():    
    if(len(listaUsuario) != 0):
        print("\n-------------Remover usuário cadastrado-------------")
        emailUsuarioCadastrado = input("\nDigite o e-mail do usuário cadastrado: ")
        verificarUsuarioExiste = False
        if emailUsuarioCadastrado != "":
            listaUsuario2 = []
            i = 0
            while i < len(listaUsuario):
                if(listaUsuario[i]['email'].upper() == emailUsuarioCadastrado.upper()):
                    print("\n-------------Usuário encontrado-------------")
                    print("\nNome: ", listaUsuario[i]['nome'], "\nE-mail:", listaUsuario[i]['email'])
                    verificarUsuarioExiste = True
                    e = 0
                    while e < len(listaUsuario):
                        if listaUsuario[e]['email'].upper() != emailUsuarioCadastrado.upper():
                            newList = {}
                            newList['nome'] = listaUsuario[e]['nome']
                            newList['email'] = listaUsuario[e]['email']
                            listaUsuario2.append(newList)
                        e= e+1
                i= i+1

            
            if(verificarUsuarioExiste == False):
                print("\n-------------Usuário não cadastrado-------------")
            else:
                print("\n-------------Usuário removido com sucesso-------------")
                if len(listaUsuario2) != 0:
                    f = 0
                    listaUsuario.clear()
                    while f < len(listaUsuario2):
                        listaUsuario.append(listaUsuario2[f])
                        f= f+1
                else:
                    listaUsuario.clear()
        else:
            print("\n-------------Erro, preencha todos os campos!-------------")
            menu()
    else:
        print("\n-------------Nenhum usuário cadastrado-------------")
    menu()
#fim remover usuario

#inicio alterar usuario
def alterarUsuario():
    if(len(listaUsuario) != 0):
        print("\n-------------Alterar usuário cadastrado-------------")
        emailUsuarioAlterar = input("\nDigite o e-mail do usuário cadastrado: ")
        verificarUsuarioAlterarExiste = False
        
        if emailUsuarioAlterar != "":
            listaUsuario2 = []
            i = 0
            while i < len(listaUsuario):
                if(listaUsuario[i]['email'].upper() == emailUsuarioAlterar.upper()):
                    print("\n-------------Usuário encontrado-------------")
                    print("\nNome: ", listaUsuario[i]['nome'], "\nE-mail:", listaUsuario[i]['email'])
                    verificarUsuarioAlterarExiste = True
                    print("\n-------------Alterar usuário-------------")
                    nomeAlterar = input('\nDigite o nome completo para alterar: ')
                    emailAlterar = input('Digite o e-mail para alterar: ')
                    if nomeAlterar != "" and emailAlterar != "":
                        e = 0
                        while e < len(listaUsuario):
                            if listaUsuario[e]['email'].upper() != emailUsuarioAlterar.upper():
                                newList = {}
                                newList['nome'] = listaUsuario[e]['nome']
                                newList['email'] = listaUsuario[e]['email']
                                listaUsuario2.append(newList)
                            elif listaUsuario[e]['email'].upper() == emailUsuarioAlterar.upper():
                                newList = {}
                                newList["nome"] = nomeAlterar.upper()
                                newList["email"] = emailAlterar.upper()
                                listaUsuario2.append(newList)
                            e= e+1
                    else:
                        print("\n-------------Erro, preencha todos os campos!-------------")
                        menu()
                        break
                i= i+1

            
            if(verificarUsuarioAlterarExiste == False):
                print("\n-------------Usuário não cadastrado-------------")
            else:
                print("\n-------------Usuário alterado com sucesso-------------")
                if len(listaUsuario2) != 0:
                    f = 0
                    listaUsuario.clear()
                    while f < len(listaUsuario2):
                        listaUsuario.append(listaUsuario2[f])
                        f= f+1
        else:
            print("\n-------------Erro, preencha todos os campos!-------------")
            menu()
    else:
        print("\n-------------Nenhum usuário cadastrado-------------")
    menu()
#fim alterar usuario

if __name__ == "__main__":
    menu()