N = 8
# Inicializa o tabuleiro
tabuleiro = [[0 for _ in range(N)] for _ in range(N)]
# Conta o número de cada movimento
contagem = 0

# Esta função representa os movimentos válidos, recebendo a posição atual do cavalo como parâmetro
def movimentos_validos(linha, coluna):
    movimentos = []
    # Par de vetores representando a movimentação do cavalo
    row_moves = [-2, -1, 1, 2, 2, 1, -1, -2]
    col_moves = [1, 2, 2, 1, -1, -2, -2, -1]
    # Laço de repetição para exibir a nova posição do cavalo
    for i in range(8):
        nova_linha = linha + row_moves[i]
        nova_coluna = coluna + col_moves[i]
        # Verifica se um movimento é possível
        if 0 <= nova_linha < N and 0 <= nova_coluna < N and tabuleiro[nova_linha][nova_coluna] == 0:
            movimentos.append((nova_linha, nova_coluna))
    return movimentos

# Soluciona o problema recursivamente, recebendo como parâmetros a posição atual do cavalo e número do movimento
def resolver(linha, coluna, num_movimento):
    global contagem
    # Crava o número do movimento na posição do tabuleiro
    tabuleiro[linha][coluna] = num_movimento
    contagem += 1
    # Se forem efetivados 64 movimentos, significa que todas as posições foram preenchidas e o problema está resolvido
    if num_movimento == N * N:
        return True

    movimentos = movimentos_validos(linha, coluna)
    # Laço for-each para efetuar todos os movimentos em caso de erro
    for mov in movimentos:
        nova_linha, nova_coluna = mov
        # Atualiza a posição do cavalo
        if resolver(nova_linha, nova_coluna, num_movimento + 1):
            return True

    # Retorna para o movimento anterior
    tabuleiro[linha][coluna] = 0
    contagem -= 1
    return False

def main():
    linha_inicial, coluna_inicial = 0, 0
    resolver(linha_inicial, coluna_inicial, 1)
    print("Número de movimentos:", contagem)
    for i in range(N):
        for j in range(N):
            print(tabuleiro[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()
