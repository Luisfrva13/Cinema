# Crie um programa de aplicativo de cinema que faça o seguinte:
# - O usuário informa nome e idade.
# - O programa mostra uma lista de 5 filmes, a sala em que cada filme está passando, e a classificação indicativa (idade mínima) de cada filme.
# - O usuário informa a sala onde está passando o filme desejado.
# - Se o usuário tiver a idade mínima para o filme, o programa imprime o ingresso e encerra a aplicação.
# - Se o usuário não tiver a idade mínima para o filme, o programa proíbe a entrada e solicita ao usuário que decida por outro filme.
import time
nome = input(f'Informe seu nome:')
idade = (input)('Informe sua idade:')

idade = int(idade)

print('LISTA DE FILMES:\n')

while True:
    print('Sala 1 - Deadpool 3 - Classificação 18 anos ')
    print('Sala 2 - Joker 2 - Classificação 16 anos')
    print('Sala 3 - Capitão América 4 - Classificação 14 anos' )
    print('Sala 4 - Divertidamente 2 - 12 anos ')
    print('Sala 5 - Moana 2 - Classficação Livre') 


    sala = (input('Informe a sala desejada: '))
    
    match sala:
        case 1 :
            if idade >= 18:
                print('O filme escolhido foi Deadpool 3, retire seu ingresso abaixo')
                break
            else:
                    print('Você não pode assistir esse filme, por favor, escolha outra opção.')
                    time.sleep (1)
                    continue
        

        case 2:
            if idade >= 16:
                print('O filme escolhido foi Joker 2, retire seu ingresso abaixo')
                break
            else:
                    print('Você não pode assistir esse filme, por favor, escolha outra opção.')
                    time.sleep (1)
                    continue
        case 3: 
            if idade >= 14:
                print('O filme escolhido foi Capitão América 2, retire seu ingresso abaixo')
                break
            else:
                    print('Você não pode assistir esse filme, por favor, escolha outra opção.')
                    time.sleep (1)
                    continue
        case 4: 
            if idade >= 12:
                print('O filme escolhido foi Divertidamente 2, retire seu ingresso abaixo')
                break
            else:
                print('Você não pode assistir esse filme, por favor, escolha outra opção.')
                time.sleep (1)
                continue
        case 5: 
            if idade >= 1:
                print('O filme escolhido foi Deadpool 3, retire seu ingresso abaixo')
                break
            else:
                    print('Você não pode assistir esse filme, por favor, escolha outra opção.')
                    time.sleep (1)
                    continue
        
    
                   
 
        
                
        