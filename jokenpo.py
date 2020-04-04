# -*- coding: utf-8 -*-
import random
from colorama import Fore, Style


def valida (valor):
    try:
        valor = abs(int(valor))
        if valor > 4:
            return None
        return valor
    except ValueError:
       pass


def arquivo(placar):
    with open('Placar.txt', 'a+') as file:          # Adicionando linhas ao arquivo, o a+ manda o cursor para o final do arquivo
        file.write(f'Rodada: {placar[0]}\n')
        file.write(f'Vencedor: {placar[4]}\n')
        file.write(f'Empate: {placar[1]} | ')
        file.write(f'Computador: {placar[2]} | ')
        file.write(f'Usuário: {placar[3]} \n ')
        file.write('-='*20+'\n')
        file.seek(0)


pt_pc = 0
pt_user = 0
empate = 0
rodada = 0
placar = []
vencedor = ''

x = True
while x:
    op = ['pedra', 'papel', 'tesoura']
    pc = random.choice(op)
    user = valida(input('Pedra [0] | Papel [1] | Tesoura [2] | Placar [3] | Sair [4]:'))

    if user is None:
        print('Valor inválido, digite um número válido!')
    else:
        if user == 3:
            print(f'Rodada {rodada} Placar:\nEmpate: {empate}\nComputador: {pt_pc}\nVocê: {pt_user}')
            rodada -= 1
        elif user == 4:
            x = False
            print('Jogo Finalizado')
            rodada -= 1
            break
        elif (pc == 'pedra' and user == 2) or (pc == 'papel' and user == 0) or (pc == 'tesoura' and user == 1):
            print(f'Você: {op[user]}\nComputador: {pc}')
            print(Fore.RED + 'Perdeu !! !')
            print(Style.RESET_ALL)
            pt_pc += 1
            vencedor = 'computador'
        elif pc == op[user]:
            print(f'Você: {op[user]}\nComputador: {pc}')
            print(Fore.BLUE + 'Empate !!')
            print(Style.RESET_ALL)
            empate += 1
            vencedor = 'empate'

        else:
            print(f'Você: {op[user]}\nComputador: {pc}')
            print(Fore.GREEN + 'Você ganhou !!')
            print(Style.RESET_ALL)
            pt_user += 1
            vencedor = 'voce'

        placar = rodada, empate, pt_pc, pt_user, vencedor

        arquivo(placar)
        rodada += 1
        print(placar)
