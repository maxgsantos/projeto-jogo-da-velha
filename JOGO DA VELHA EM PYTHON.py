def retorna_jog_maquina(jog_em_questao):
    global tabuleiro, _jogadaInvalida
    valor_atual = jog_em_questao
    jogada_val_retorno = 0
    
    if (tabuleiro[7] + tabuleiro[8] + tabuleiro[9]) == (2 * valor_atual):
        if tabuleiro[7] == 0:
            jogada_val_retorno = 7
        elif tabuleiro[8] == 0:
            jogada_val_retorno = 8
        else:
            jogada_val_retorno = 9
    elif (tabuleiro[4] + tabuleiro[5] + tabuleiro[6]) == (2 * valor_atual):
        if tabuleiro[4] == 0:
            jogada_val_retorno = 4
        elif tabuleiro[5] == 0:
            jogada_val_retorno = 5
        else:
            jogada_val_retorno = 6
    elif (tabuleiro[1] + tabuleiro[2] + tabuleiro[3]) == (2 * valor_atual):
        if tabuleiro[1] == 0:
            jogada_val_retorno = 1
        elif tabuleiro[2] == 0:
            jogada_val_retorno = 2
        else:
            jogada_val_retorno = 3
    elif (tabuleiro[7] + tabuleiro[4] + tabuleiro[1]) == (2 * valor_atual):
        if tabuleiro[7] == 0:
            jogada_val_retorno = 7
        elif tabuleiro[4] == 0:
            jogada_val_retorno = 4
        else:
            jogada_val_retorno = 1
    elif (tabuleiro[8] + tabuleiro[5] + tabuleiro[2]) == (2 * valor_atual):
        if tabuleiro[8] == 0:
            jogada_val_retorno = 8
        elif tabuleiro[5] == 0:
            jogada_val_retorno = 5
        else:
            jogada_val_retorno = 2
    elif (tabuleiro[9] + tabuleiro[6] + tabuleiro[3]) == (2 * valor_atual):
        if tabuleiro[9] == 0:
            jogada_val_retorno = 9
        elif tabuleiro[6] == 0:
            jogada_val_retorno = 6
        else:
            jogada_val_retorno = 3
    elif (tabuleiro[7] + tabuleiro[5] + tabuleiro[3]) == (2 * valor_atual):
        if tabuleiro[7] == 0:
            return 7
        elif tabuleiro[5] == 0:
            jogada_val_retorno = 5
        else:
            jogada_val_retorno = 3
    elif (tabuleiro[9] + tabuleiro[5] + tabuleiro[1]) == (2 * valor_atual):
        if tabuleiro[9] == 0:
            jogada_val_retorno = 9
        elif tabuleiro[5] == 0:
            jogada_val_retorno = 5
        else:
            jogada_val_retorno = 1

    if jogada_val_retorno != 0:
        return jogada_val_retorno
    else:
        return _jogadaInvalida

def jogada_da_maquina():
    global num_de_jogadas, jogador_atual, tabuleiro, _jogadaInvalida
    jogada_val = 0
    if num_de_jogadas == 9:
        jogada_val = -1
        return jogada_val

    jogada_val_temp = retorna_jog_maquina(jogador_atual)
    if jogada_val_temp != _jogadaInvalida:
        jogada_val = jogada_val_temp

    outro_jogador = retorna_outro_jogador(jogador_atual)
    jogada_val_temp = retorna_jog_maquina(outro_jogador)
    if jogada_val_temp != _jogadaInvalida and jogada_val == 0:
        jogada_val = jogada_val_temp
        return jogada_val

    if num_de_jogadas == 3 and jogada_val == 0:
        if (tabuleiro[1] * tabuleiro[9] == 1 or tabuleiro[3] * tabuleiro[7] == 1) and tabuleiro[5] != 0:
            jogada_val = 1
            return jogada_val
        if (tabuleiro[2] * tabuleiro[9] == 1 or tabuleiro[1] * tabuleiro[6] == 1 or tabuleiro[2] * tabuleiro[6] == 1) and tabuleiro[5] != 0:
            jogada_val = 2
            return jogada_val

    if num_de_jogadas <= 2 and jogada_val == 0:
        if tabuleiro[5] == 0:
            jogada_val = 5
        elif tabuleiro[1] == 0:
            jogada_val = 1
        else:
            jogada_val = 8
    else:
        if jogada_val == 0:
            jogada_val = _jogadaInvalida
            if tabuleiro[5] == 0:
                jogada_val = 5
            elif tabuleiro[7] == 0:
                jogada_val = 7
            elif tabuleiro[9] == 0:
                jogada_val = 9
            elif tabuleiro[1] == 0:
                jogada_val = 1
            elif tabuleiro[3] == 0:
                jogada_val = 3
        if jogada_val != _jogadaInvalida:
            return jogada_val

    pupula_lista_de_jog_valid()
    jog_valid = lista_jog_valid[1]

    if jog_valid == 1:
        jogada_val = lista_jog_valid[2]
        return jogada_val

    if jogada_val != 0:
        return jogada_val
    else:
        jog_valid = lista_jog_valid[2]
        return jog_valid

def pupula_lista_de_jog_valid():
    global lista_jog_valid, tabuleiro
    lista_jog_valid = [0] * 11

    lista_jog_valid[1] = 0
    for i in range(1, 10):
        if tabuleiro[i] == 0:
            lista_jog_valid[1] += 1
            lista_jog_valid[lista_jog_valid[1] + 1] = i

def retorna_outro_jogador(jogador):
    return 1 if jogador == -1 else -1

def cabecalho():
    print("#JOGO DA VELHA#")
    print(" ")

def limpar_variaveis():
    global tabuleiro, posicao_do_vet
    posicao_do_vet = [[" "] * 4 for _ in range(4)]
    tabuleiro = [0] * 10

def exibir_tabuleiro():
    global posicao_do_vet
    print(f" {posicao_do_vet[1][1]} | {posicao_do_vet[1][2]} | {posicao_do_vet[1][3]} ")
    print("---+---+---")
    print(f" {posicao_do_vet[2][1]} | {posicao_do_vet[2][2]} | {posicao_do_vet[2][3]} ")
    print("---+---+---")
    print(f" {posicao_do_vet[3][1]} | {posicao_do_vet[3][2]} | {posicao_do_vet[3][3]} ")

def verifica_ganhador():
    global alguem_ganhou, tabuleiro, jogador_atual, ganhador, cont_coluna, cont_linha, jogadorX, jogadorO
    if cont_coluna >= 3:
        alguem_ganhou = True

    for i in range(1, 4):
        cont_linha = 0
        cont_coluna = 0
        for j in range(1, 4):
            if tabuleiro[3 * i - j] == jogador_atual:
                cont_linha += 1
            if tabuleiro[3 * j - i] == jogador_atual:
                cont_coluna += 1
            if cont_linha >= 3:
                alguem_ganhou = True

    if cont_linha == 3:
        alguem_ganhou = True

    if tabuleiro[1] == jogador_atual and tabuleiro[5] == jogador_atual and tabuleiro[9] == jogador_atual:
        alguem_ganhou = True

    if tabuleiro[3] == jogador_atual and tabuleiro[5] == jogador_atual and tabuleiro[7] == jogador_atual:
        alguem_ganhou = True

    if alguem_ganhou:
        ganhador = jogadorX if jogador_atual == 1 else jogadorO

def parabens():
    global alguem_ganhou, ganhador
    if not alguem_ganhou:
        print("Empate!")
        return

    print(f"Parabéns {ganhador}, você venceu!")
    alguem_ganhou = True

# Variáveis globais
tabuleiro = [0] * 10
jogador_atual = 1
alguem_ganhou = False
ganhador = ""
jogadorX = "X"
jogadorO = "O"
num_de_jogadas = 0
cont_coluna = 0
cont_linha = 0
_jogadaInvalida = -9999
lista_jog_valid = [0] * 11
posicao_do_vet = [[" "] * 4 for _ in range(4)]

# Execução principal
if __name__ == "__main__":
    cabecalho()
    limpar_variaveis()
    exibir_tabuleiro()

    while True:
        if jogador_atual == -1:
            jogada = jogada_da_maquina()
            if jogada == -1:
                break
            tabuleiro[jogada] = jogador_atual
        else:
            jogada = int(input("Escolha sua jogada (1-9): "))
            if tabuleiro[jogada] != 0:
                print("Jogada inválida. Tente novamente.")
                continue
            tabuleiro[jogada] = jogador_atual

        num_de_jogadas += 1
        posicao_do_vet[(jogada - 1) // 3 + 1][(jogada - 1) % 3 + 1] = "X" if jogador_atual == 1 else "O"
        exibir_tabuleiro()
        verifica_ganhador()

        if alguem_ganhou:
            parabens()
            break

        jogador_atual = retorna_outro_jogador(jogador_atual)