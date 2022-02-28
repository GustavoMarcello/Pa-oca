# ==================================================
# Este programa tem o objetivo de auxiliar de
# maneira didática alunos na alfabetização a 
# partir do jogo "Paçoca", inspirado no jogo 
# https://term.ooo
# ==================================================

from data_palavras import total_palavras, palavras_jogo
from random import randint

n = randint(0, 2)
palavra = palavras_jogo[n]
tentativas = 0

escolha = input('\033[1;35mDigite uma palavra com 6 letras\033[m\n').upper()
while True:
    if escolha not in total_palavras:
        print('Palavra inválida, tente novamente:\n')
    else:
        escolha_lista = list(escolha)
        acertos = 0
        tentativas += 1
        for i in range(0, 6):
            escolha_lista[i] = f'\033[1;33m{escolha[i]}\033[m ' if escolha[i] in palavra else f'\033[1;31m{escolha[i]}\033[m '
            if escolha[i] == palavra[i]:
                escolha_lista[i] = f'\033[1;34m{escolha[i]}\033[m '
                acertos += 1
        resultado = "".join(escolha_lista)
            
        print(resultado)
        if acertos == 6:
            print(f'\033[1;35mParabéns, você acertou em \033[1;31m{tentativas}\033[m \033[1;35mtentativas\033[m')
            break
    escolha = input('').upper()
    
        