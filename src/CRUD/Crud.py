from funcoes import Funcoes
from bancoDeDados import Banco

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

    procurarEmailUsuraio = input("Digite o email do usuário: ").lower()

    #variavél usada para controlar a remoção do usuário cadastrado, caso ele exista ele poderá ser removido.
    encontrado = False

    for usuarioEmail in Banco.listaDeUsuarios:
                
        #se o usuário existir, ele pergunta se você quer realmente remover o usuário.
        if usuarioEmail["email"].lower() == procurarEmailUsuraio:

            encontrado = True
            confirmacao = input(f"Você deseja remover o usuário {usuarioEmail}? ").lower()

            if confirmacao in ["sim", "s", "ss"]:

                Banco.listaDeUsuarios.remove(usuarioEmail)
                Banco.salvarUsuario()
                print("Usuário removido")

            elif confirmacao in ["não","nao","n","nn"]:

                print("Remoção cancelada.")
            else:

                print("Não entendi o comando, utilize sim ou não! ")
            break

    if not encontrado:
        print("Desculpe, mas não foi possível remover o usuário pois o mesmo não foi encontrado na nossa lista.")
