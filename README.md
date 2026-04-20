--Sistema de gerenciamento de usuários(CLI)--
Este projeto permite gerenciar usuários através do terminal.
O sistema permite cadastro, listar, buscar e remover usuários de forma interativa.

--Estrutura do projeto--
O sistema funciona com uma lista de usuários, onde cada usuário é representado por um dicionário:
-Nome
-Idade
-Email

Exemplo:
[ {"nome": "Ana", "idade": 20, "email": "ana@gmail.com"} ]

--Validações implementadas--
-O programa não permite usuários com nomes duplicados
-Verifica se o valor digitado no menu é válido
-Trata erros quando o usuário digita letras ao invés de números

--Melhorias futuras--
-Adicionar validação de email
-Adicionar editar usuário
-Adicionar um ID único para cada usuário

--Objetivo do projeto--
Este projeto foi desenvolvido com o objetivo de praticar:
-Lógica de programação
-Manipulação de listas e dicionários
-Estrturas de repetição
-Controle de fluxo
-Boas práticas iniciais em Python

--Melhorias feitas--
-Salvar os dados em arquivo (JSON ou banco de dados)
-Separar o código em funções
-Melhorar a exibição dos usuários (formatação mais amigável)
-Foi alterado o verificador do nome para o email.
-Foi adicionado  um condicional para verificar o valor de idade.

--Autor

Projeto desenvolvido para fins de aprendizado em Python.