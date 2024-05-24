# Crie um programa de aplicativo de cinema que faça o seguinte:
# - O usuário informa nome e idade.
# - O programa mostra uma lista de 5 filmes, a sala em que cada filme está passando, e a classificação indicativa (idade mínima) de cada filme.
# - O usuário informa a sala onde está passando o filme desejado.
# - Se o u
# suário tiver a idade mínima para o filme, o programa imprime o ingresso e encerra a aplicação.
# - Se o usuário não tiver a idade mínima para o filme, o programa proíbe a entrada e solicita ao usuário que decida por outro filme.

# importa biblioteca
import os

# recebe o nome do usuário e a idade
nome = input('Informe o seu nome: ')
idade = int(input('Informe a sua idade: '))

# limpa console
os.system('cls')

# inicia o loop
while True:
    # exibe a lista de filmes e suas salas
    print(f'{'-'*20}Filmes em cartaz{'-'*20}\n')
    print('Sala 1 - Joker 2 . - 16 anos.')
    print('Sala 2 - Divertidamente 2. - 12 anos.')
    print('Sala 3 - Capitão America 4. - 14 anos.')
    print('Sala 4 - Moana 2. - Livre')
    print('Sala 5 - Deadpool 3. - 18 anos.')

    # recebe a sala escolhida
    sala = input('Informe a sala desejada: ')

    # limpa console
    os.system('cls')

    # verifica a sala e a idade
    match sala:
        case '1':
            idade_minima = 16
        case '2':
            idade_minima = 12
        case '3':
            idade_minima = 14
        case '4':
            idade_minima = 0
        case '5':
            idade_minima = 18
        case _:
            print('Sala inexistente.')
            continue
    
    if idade >= idade_minima:
        print(f'Ingresso liberado para {nome}. Bom filme!')
        break
    else:
        print(f'Entrada não permitida para {nome}. Favor escolher outro filme!')
        continue