# Jogo Nim
# Desenvolvido por William Persch e Cristiano Ledur
import random
from time import sleep
palitos = 0
min_palitos = 0
max_palitos = 5
jogadores = []
venceu = ''
def tempo(segundos):
    for i in range(0,segundos):
        sleep(1)
while True:
    start = input("Jogar contra Colega ou contra o Computador? ")
    if start.lower() == 'colega':
        jogador1 = input("Informe o nome do 1° jogador: ")
        jogador2 = input("Informe o nome do 2° jogador: ")
        jogadores.insert(0, jogador1)
        jogadores.insert(1, jogador2)
        break
    elif start.lower() == 'computador':
        jogador = input("Informe seu nome: ")
        jogadores.insert(0, jogador)
        jogadores.insert(1, 'Computador')
        break
 
while palitos >= 40 or palitos <= 4 or palitos % 2 == 0:
    print("Escolha um número impar entre 5 e 39 para ser a quantidade de palitos: ")
    palitos = int(input())
    if palitos >= 40 or palitos <= 4 or palitos % 2 == 0:
        print("Lembrando que a quantidade de palitos deve ser um número IMPAR entre 5 e 39!")

while min_palitos <= 0 or min_palitos < 1 or min_palitos > 3:
    min_palitos = int(input("Entre 1 a 3, informe a quantidade MÍNIMA de palitos a serem removidos por jogada: "))
        
while max_palitos >= 5 or max_palitos < 2 or min_palitos >= max_palitos:
    if min_palitos == 3:
        max_palitos = 4
        tempo(1)
        print("4 é a maior quantidade de palitos a serem removidos por jogada!")
        break
    print(f'Escolha um número entre {min_palitos+1} e 4 para ser a quantidade MÁXIMA de palitos a serem removidos por jogada:')
    max_palitos = int(input())
tempo(1)
print('\n'  ,"Tudo pronto! Podemos começar...")

if start.lower() == 'computador' or start.lower() == 'colega':
    valida_final = False
    while True:
        for indice in range(len(jogadores)):
            jogada_maquina = random.randint(min_palitos, max_palitos)
            if palitos < 1:
                venceu = jogadores[indice]
                valida_final = True 
                break
            tempo(1)
            print('\n',f'Restam {palitos} palitos:','\n','\n',palitos * '|','\n')
            tempo(1)
            if indice == 0 or jogadores[indice] != 'Computador':
                print(f'{jogadores[indice]}, escolha a quantidade de palitos que você quer remover: ')
                jogada = int(input())
                while jogada < min_palitos or jogada > max_palitos:
                    print(f'Sendo {min_palitos} a menor quantidade possível e {max_palitos} a maior. {jogadores[indice]}, escolha a quantidade de palitos que você quer remover: ')
                    jogada = int(input())
                print('\n',f'{jogadores[indice]} removeu {jogada} palitos.')
                if jogada >= min_palitos and jogada <= max_palitos:
                    palitos -= jogada
            elif jogadores[indice] == 'Computador':
                tempo(1)
                print(f'{jogadores[indice]} removeu {jogada_maquina} palitos.')
                palitos -= jogada_maquina
        if valida_final == True:
            break
            
print('\n',f'{"*" * 10} Final da partida {"*" * 10}','\n')
print(f'{venceu} foi o vencedor!')

with open('partidas.txt', 'r+', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    arquivo.writelines(f'\nJogador 1: {jogadores[0]}\nJogador 2: {jogadores[1]}\nVencedor: {venceu}')
    arquivo.writelines(f'\n<{"="*20}>')