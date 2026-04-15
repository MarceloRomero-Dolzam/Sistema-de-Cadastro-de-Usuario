listaDeUsuarios = [
    {"nome": "Ana", "idade": 20, "email": "ana@gmail.com"}
]



while True:

    print("Escolha uma opção:\n"
                            "1 - Cadastrar usuário\n"
                            "2 - Listar usuário\n"
                            "3 - Buscar usuário\n"
                            "4 - Remover usuário\n"
                            "5 - sair\n")

    try:
        menuDeOpcoes = int(input("Digite sua opção: "))
    

        if menuDeOpcoes < 1 or menuDeOpcoes > 5:

            print("Escolha entre as opções 1 e 5.")
        
        #adiciona usuário
        elif menuDeOpcoes == 1:

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

                idade = int(input("Digite a idade: "))
                email = input("Digite o email: ")

                usuario = {
                    "nome": nome,
                    "idade": idade,
                    "email": email
                }

                #adiciona o novo usuário à lista.
                listaDeUsuarios.append(usuario)

        #mostra a lista de usuários
        elif menuDeOpcoes == 2:

            print(f"{listaDeUsuarios}")

        #busca o usuário
        elif menuDeOpcoes == 3:
            
            buscarNomeUsuario = input("Digite o nome do usuário: ").lower()

            #variavél criada para ajduar no controle de busca, se ele existir no sistema a variavél retorna True.
            encontrado = False

            #procura o usuário na lista do sistema.
            for usuarioNome in listaDeUsuarios:

                if usuarioNome["nome"].lower() == buscarNomeUsuario:
                    print(f"Usuário encontrado:\n {usuarioNome}")
                    encontrado = True
                    break

            if not encontrado:
                print("Usuário não encontrado.")
                
            
        #remove o usuário
        elif menuDeOpcoes == 4:

            procurarNomeUsuraio = input("Digite o nome do usuário: ").lower()

            #variavél usada para controlar a remoção do usuário cadastrado, caso ele exista ele poderá ser removido.
            NomeEncontrado = False

            for usuarioNome in listaDeUsuarios:
                
                #se o usuário existir, ele pergunta se você quer realmente remover o usuário.
                if usuarioNome["nome"].lower() == procurarNomeUsuraio:

                    removerUsuario = input(f"Você deseja remover o usuário {usuarioNome}? ").lower()

                    if removerUsuario == "sim" or removerUsuario == "s":
                        listaDeUsuarios.remove(usuarioNome)
                        print("Usuário removido")
                        NomeEncontrado = True
                        break

            if not NomeEncontrado:
                print("Desculpe, mas não foi possível remover o usuário pois o mesmo não encontrado na nossa lista.")

        #Sai do programa.
        elif menuDeOpcoes == 5:

            print("saindo da lista.")
            break
    
    except ValueError:
        print("As partes do programa que só aceitam número, como em idade - na parte de cadastro -  e "
              "na lista de opções.")