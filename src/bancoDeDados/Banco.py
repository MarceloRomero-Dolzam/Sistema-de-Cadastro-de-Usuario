import json
import os

listaDeUsuarios = []
arquivo = 'src/bancoDeDados/BancoDeDadosUsuario.json'

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

listaDeUsuarios = carregarUsuario()

def salvarUsuario():
    with open(arquivo, 'w', encoding = 'utf-8') as dados:
        json.dump(listaDeUsuarios, dados, indent = 4)