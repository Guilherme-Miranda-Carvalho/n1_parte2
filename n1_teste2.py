def criarUsuario():  # Função para criar usuário
    novoUsuario= {} 
    novoUsuario["nomeCompleto"] = input('Digite o seu nome completo: ')
    novoUsuario["email"] = input('Digite o seu email: ')
    return novoUsuario #Vai retornar o dicionário   

def exibirNomeAlunosCadastrados(listaUsuarioCadastrado: list):
    for umUsuario in listaUsuarioCadastrado:
        print("Nome do usuário: ", umUsuario["nomeCompleto"])
        print("Email: ", umUsuario["email"])

def exibirNomesAlunosOrdemAlfabetica(listaUsuarioCadastrado: list):
    ordenada = list(listaUsuarioCadastrado)
    ordenada.sort()
    for key in ordenada:
        print(key)

def verificarSeExisteAluno(listaUsuarioCadastrado):
    verificacao = input("Digite o nome que deseja pesquisar: ")
    if listaUsuarioCadastrado["nomeCompleto"] == verificacao:
        print("Aluno matriculado na instituição")
    else :
        print('Não está matriculado na instituição')
        
    
    def main():
    
    listaUsuarioCadastrado = []

    print('Cadastro do usuário')
    listaUsuarioCadastrado.append(criarUsuario())

    novocadastro = input('Gostaria de cadastrar um novo usuário? Digite 1 para sim e 2 para Não. ')
    while novocadastro == "1":
        listaUsuarioCadastrado.append(criarUsuario())
        novocadastro = input('Gostaria de cadastrar um novo usuário? Digite 1 para sim e 2 para Não. ')

    exibirNomeAlunosCadastrados(listaUsuarioCadastrado)
    verificarSeExisteAluno(listaUsuarioCadastrado)
    exibirNomesAlunosOrdemAlfabetica(listaUsuarioCadastrado)
   


if __name__ == "__main__":
    main()
