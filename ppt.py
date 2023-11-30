import random

def jogar():
    user = input("Escolha entre: 'pd' para pedra, 'pp' para papel, 'ts' para tesoura: ")
    computer = random.choice(['pd','pp','ts'])

    if user == computer:
        return 'Deu empate!'

# pd > ts, ts > pp, pp >pd
    if vencer(user, computer):
        return 'Você venceu!'

    return 'Você perdeu!'


def vencer (jogador, oponente):
    #retorna TRUE se o jogador vencer
    if (jogador == 'pd' and oponente == 'ts') or (jogador == 'ts' and oponente == 'pp') or (jogador == 'pp' and oponente == 'pd'):
        return True

print(jogar())