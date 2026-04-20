import json
import os

listaDeUsuarios = []
arquivo = 'BancoDeDadosUsuario.json'

def carregarUsuario():

    #o os.path.exists() verifica se existe um arquivo em específico.
    if os.path.exists(arquivo):

        #o with serve para arbir este arquivo e fecha-lo. 
        #O 'r' serve para ler o arquivo.
        #O o as serve para nomear uma ferramenta que possui um nome extenso com um nome curto.
        #O enconding = 'utf-8' evita problema com acentos.
        with open(arquivo, 'r', encoding = 'utf-8') as dados:

            #Utilziado para tratar qualquer erro que possa aparecer no arquivo.
            try:
                listaDeUsuarios = json.load(dados)
            except json.JSONDecodeError:
                print("Erro ao ler o banco de dados!")
                #em caso de erro, ele retorna a lista vazia.
                listaDeUsuarios = []

            if not isinstance(listaDeUsuarios, list):

                listaDeUsuarios = []

    else:
        listaDeUsuarios = []

    return listaDeUsuarios 

#para ativar a def
listaDeUsuarios = carregarUsuario()  

def salvarUsuario():
    with open(arquivo, 'w', encoding = 'utf-8') as dados:
        json.dump(listaDeUsuarios, dados, indent = 4)

def AddUsuario():
    nome = input("Digite o nome: ")

    #variavél criada para previnir nomes repetidos.
    jaExiste = False

    #verifica se há nomes repetidos.
    for nomeRepetido in listaDeUsuarios:
                
        #se existir nomes repetidos ele avisa, mostra o usuário existente e sai do programa(break)
        if nomeRepetido["nome"].lower() == nome.lower():
            print(f"Já existe um usuário com este nome:\n {nomeRepetido}")
            jaExiste = True
            break
                
    #se não existir, ele continua o programa normalmente.
    if not jaExiste:
        try:
            idade = int(input("Digite a idade: "))
        except ValueError:
            print("O campo 'idade' só aceita números.")
        
        email = input("Digite o email: ")

        usuario = {
            "nome": nome,
            "idade": idade,
            "email": email
        }

        #adiciona o novo usuário à lista.
        listaDeUsuarios.append(usuario)
        salvarUsuario()

        print("Usuário cadastrado com sucesso!")

def buscarUsuario():
    buscarNomeUsuario = input("Digite o nome do usuário: ").lower()

    #variavél criada para ajduar no controle de busca, se ele existir no sistema a variavél retorna True.
    encontrado = False

    #procura o usuário na lista do sistema.
    for usuarioNome in listaDeUsuarios:

        if usuarioNome["nome"].lower() == buscarNomeUsuario:
            print("\n--Usuário encontrado--")
            usuarioFormatado(usuarioNome)
            encontrado = True
            break

    if not encontrado:
        print("Usuário não encontrado.")

def removerUsuario():

    procurarNomeUsuraio = input("Digite o nome do usuário: ").lower()

    #variavél usada para controlar a remoção do usuário cadastrado, caso ele exista ele poderá ser removido.
    encontrado = False

    for usuarioNome in listaDeUsuarios:
                
        #se o usuário existir, ele pergunta se você quer realmente remover o usuário.
        if usuarioNome["nome"].lower() == procurarNomeUsuraio:

            encontrado = True
            confirmacao = input(f"Você deseja remover o usuário {usuarioNome}? ").lower()

            if confirmacao in ["sim", "s", "ss"]:

                listaDeUsuarios.remove(usuarioNome)
                salvarUsuario()
                print("Usuário removido")

            elif confirmacao in ["não","nao","n","nn"]:

                print("Remoção cancelada.")
            else:

                print("Não entendi o comando, utilize sim ou não! ")
            break

    if not encontrado:
        print("Desculpe, mas não foi possível remover o usuário pois o mesmo não encontrado na nossa lista.")

def usuarioFormatado(usuario):

    print(f"Nome: {usuario['nome']}")
    print(f"Idade: {usuario['idade']}")
    print(f"Email: {usuario['email']}")
    print("---------------------------")


while True:

    print("Escolha uma opção:\n"
                            "1 - Cadastrar usuário\n"
                            "2 - Listar usuário\n"
                            "3 - Buscar usuário\n"
                            "4 - Remover usuário\n"
                            "5 - sair\n")

    try:
        menuDeOpcoes = int(input("Digite sua opção: "))
    except ValueError:
        print("O campo de 'Digite sua opção:' só aceita números")

        if menuDeOpcoes < 1 or menuDeOpcoes > 5:

            print("Escolha entre as opções 1 e 5.")
        
        #adiciona usuário
        elif menuDeOpcoes == 1:

           AddUsuario()

        #mostra a lista de usuários
        elif menuDeOpcoes == 2:
            
            #se a lista de usuários estiver vázia.
            if not listaDeUsuarios:

                print("Nenhum usuário cadastrado.")
            #caso ela não esteja vázia.
            else:

                for usuario in listaDeUsuarios:

                    usuarioFormatado(usuario)

        #busca o usuário
        elif menuDeOpcoes == 3:
            
           buscarUsuario()
        
        #remove o usuário
        elif menuDeOpcoes == 4:

            removerUsuario()
            
        #Sai do programa.
        elif menuDeOpcoes == 5:

            print("saindo da lista.")
            break
