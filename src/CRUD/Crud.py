from bancoDeDados import Banco
from funcoes import Funcoes

def AddUsuario():

    while True:
        nome = input("Digite o nome: ")

        if not Funcoes.validarNome(nome):
            print("O nome está no formato incorreto, ele precisa respeitar a regra de carater: de 'Aa' a 'Zz' e com, no mínimo, 5 caracters")
        else:
            break




    while True:

        email = input("Digite o email: ").lower().strip()

        #variavél criada para previnir emails repetidos.
        existe = False
        

        if not Funcoes.validarEmail(email):

            print("Email inválido! Tente inserir o email novamente")
        else:
            #verifica se há emails repetidos.
            for emailRepetido in Banco.listaDeUsuarios:
                    
                #se existir emails repetidos ele avisa, mostra o email existente e sai do programa(break)
                if emailRepetido["email"] == email.lower().strip():
                    existe = True

            if existe:

                print(f"Já existe um usuário com este email.")
            else: 
                break

        
                
    #se não existir, ele continua o programa normalmente.
    if not existe:

        while True:

            try:
                idade = int(input("Digite a idade: "))

                if idade <= 0:
                    print("Digite uma idade maior que 0.")
                elif idade >= 100:
                    print("Digite uma idade menor que 100.")
                else:
                    break
            except ValueError:
                print("O campo 'idade' só aceita números.")

        usuario = {
            "nome": nome,
            "idade": idade,
            "email": email
        }

        #adiciona o novo usuário à lista.
        Banco.listaDeUsuarios.append(usuario)
        Banco.salvarUsuario()

        print("Usuário cadastrado com sucesso!")

def removerUsuario():

    procurarEmailUsuraio = input("Digite o email do usuário: ").lower().strip()

    #variavél usada para controlar a remoção do usuário cadastrado, caso ele exista ele poderá ser removido.
    encontrado = False

    for usuario in Banco.listaDeUsuarios:
                
        #se o usuário existir, ele pergunta se você quer realmente remover o usuário.
        if usuario["email"] == procurarEmailUsuraio:

            encontrado = True
            Funcoes.usuarioFormatado(usuario)
            confirmacao = input("Você deseja remover o usuário? ").lower()

            if confirmacao in ["sim", "s", "ss"]:

                Banco.listaDeUsuarios.remove(usuario)
                Banco.salvarUsuario()
                print("Usuário removido")

            elif confirmacao in ["não","nao","n","nn"]:

                print("Remoção cancelada.")
            else:

                print("Não entendi o comando, utilize sim ou não!")
            break

    if not encontrado:
        print("Desculpe, mas não foi possível remover o usuário pois o mesmo não foi encontrado na nossa lista.")

def editarUsuario():
    buscaremailUsuario = input("Digite o email do usuario: ").lower().strip()
    encontrado = False

    for emailUsuario in Banco.listaDeUsuarios:
        
        if emailUsuario["email"].lower() == buscaremailUsuario:

            encontrado = True

            Funcoes.usuarioFormatado(emailUsuario)
            confirmacao = input("Você deseja editar esse usuário: ").lower()

            if confirmacao in ["ss", "s", "sim"]:

                while True:
                    print("Escolha uma opção:\n"
                            "1 - Editar nome\n"
                            "2 - Editar email\n"
                            "3 - Editar idade\n"
                            "4 - Sair\n"
                        )

                    try:

                        editarCampo = int(input("Digite sua opção: "))

                        if editarCampo < 1 or editarCampo > 4:
                            print("Escolha entre as opções 1 e 4.")
                        
                        elif editarCampo == 1:
                            
                            while True:

                                novoNome = input("Digite o novo nome:")

                                if not Funcoes.validarNome(novoNome):

                                    print("O nome está no formato incorreto, ele precisa respeitar a regra de carater: "
                                            "de 'Aa' a 'Zz' e com, no mínimo, 5 caracters"
                                        )
                                else:

                                    break

                            emailUsuario["nome"] = novoNome
                            Banco.salvarUsuario()
                            print("Nome atualziado.")

                        elif editarCampo == 2:
                            
                            
                            while True:

                                novoEmail = input("Digite o novo email: ").lower().strip()
                                if not Funcoes.validarEmail(novoEmail):

                                    print("Email inválido! Tente inserir o email novamente")

                                elif Funcoes.verificarEmailRepetido(novoEmail):
                                    print("este email já existe no nosso sistema, digite outro.")

                                else:
                                    
                                    break

                            emailUsuario["email"] = novoEmail
                            Banco.salvarUsuario()
                            print("Email atualziado")
                        
                        elif editarCampo == 3:

                            try:
                            
                                novaIdade = int(input("Digite a idade: "))

                                if novaIdade > 0 and novaIdade < 100:

                                    emailUsuario["idade"] = novaIdade
                                    Banco.salvarUsuario()
                                    print("Idade atualizada")
                                else:

                                    print("Idade inválida.")

                            except ValueError:
                                print("O campo de 'Digite a idade:' só aceita números")
                            
                        if editarCampo == 4:

                            break

                    except ValueError:
                        print("O campo de 'Digite sua opção:' só aceita números")

            elif confirmacao in ["não","nao","n","nn"]:

                print("Remoção cancelada.")
            else:

                print("Não entendi o comando, utilize sim ou não!")
            break

    if not encontrado:
        print("Usuário não foi encontrado.")