from funcoes import Funcoes
from bancoDeDados import Banco
from CRUD import Crud

while True:

    print("---------------------------")
    print("Escolha uma opção:\n"
                            "1 - Cadastrar usuário\n"
                            "2 - Listar usuário\n"
                            "3 - Buscar usuário\n"
                            "4 - Remover usuário\n"
                            "5 - Editar usuário\n"
                            "6 - sair\n")

    try:
        menuDeOpcoes = int(input("Digite sua opção: "))


        if menuDeOpcoes < 1 or menuDeOpcoes > 6:

            print("Escolha entre as opções 1 e 6.")
        
        #adiciona usuário
        elif menuDeOpcoes == 1:
            print("---------------------------")
            Crud.AddUsuario()

        #mostra a lista de usuários
        elif menuDeOpcoes == 2:
            
            #se a lista de usuários estiver vázia.
            if not Banco.listaDeUsuarios:

                print("Nenhum usuário cadastrado.")
            #caso ela não esteja vázia.
            else:

                for usuario in Banco.listaDeUsuarios:

                    Funcoes.usuarioFormatado(usuario)

        #busca o usuário
        elif menuDeOpcoes == 3:
            print("---------------------------")
            Funcoes.buscarUsuario()
        
        #remove o usuário
        elif menuDeOpcoes == 4:
            print("---------------------------")
            Crud.removerUsuario()
        
        #edita o usuário
        elif menuDeOpcoes == 5:
            print("---------------------------")
            Crud.editarUsuario()

        #Sai do programa.
        elif menuDeOpcoes == 6:

            print("saindo da lista.")
            break
    
    except ValueError:
        print("O campo de 'Digite sua opção:' só aceita números")