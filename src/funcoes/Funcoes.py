import re
from bancoDeDados import Banco

def validarEmail(email):

    padrãoEmail = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    valido = False
    #re.match serve para verificar um padrão.
    if re.match(padrãoEmail, email):

        valido = True
    else:

        valido = False

    return valido

def validarNome(nome):

    padraoNome = r"^[a-zA-ZÀ-ÖØ-öø-ÿ]+(?:[ \s-][a-zA-ZÀ-ÖØ-öø-ÿ]+)*$";
    nomeStrip = nome.strip()
    nomeValido = False
    #re.fullmatch verifica a string completa e compara ela com o padrão desejado.
    if not re.fullmatch(padraoNome, nomeStrip) or len(nomeStrip) < 5:

        nomeValido = False
    else:

        nomeValido = True

    return nomeValido


def verificarEmailRepetido(email):

    emailRepetido = False

    for usuario in Banco.listaDeUsuarios:

        if usuario["email"] == email:

            emailRepetido = True

    return emailRepetido


def buscarUsuario():
    buscarEmail = input("Digite o email do usuário: ").lower().strip()

    #variavél criada para ajduar no controle de busca, se ele existir no sistema a variavél retorna True.
    encontrado = False

    #procura o usuário na lista do sistema.
    for usuarioEmail in Banco.listaDeUsuarios:

        if usuarioEmail["email"].lower() == buscarEmail:
            print("\n--Usuário encontrado--")
            usuarioFormatado(usuarioEmail)
            encontrado = True
            break

    if not encontrado:
        print("Usuário não encontrado.")

def usuarioFormatado(usuario):

    print("---------------------------")
    print(f"Nome: {usuario['nome']}")
    print(f"Idade: {usuario['idade']}")
    print(f"Email: {usuario['email']}")