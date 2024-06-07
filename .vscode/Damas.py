N = 8

tabuleiro = [[0 for _ in range(N)] for _ in range(N)]

# Verifica se é seguro colocar uma rainha na posição tabuleiro[linha][coluna]
def is_seguro(linha, coluna):
    for i in range(coluna):                                                                  
        if tabuleiro[linha][i] == 1:
            return False

    i, j = linha, coluna
    while i >= 0 and j >= 0:                                                                
        if tabuleiro[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = linha, coluna
    while i < N and j >= 0:                                                                 
        if tabuleiro[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

# Resolve o problema das oito rainhas usando backtracking
def resolver_nq_util(coluna):
    if coluna >= N:
        return True

    for i in range(N):
        if is_seguro(i, coluna):
            tabuleiro[i][coluna] = 1
            imprimir_tabuleiro()
            if resolver_nq_util(coluna + 1):
                return True
            tabuleiro[i][coluna] = 0
            imprimir_tabuleiro()

    return False

# Imprime o tabuleiro
def imprimir_tabuleiro():
    for i in range(N):
        for j in range(N):
            print(tabuleiro[i][j], end=" ")
        print()
    print("-------")

# Resolve o problema das oito rainhas e imprime a solução
def resolver_nq():
    if not resolver_nq_util(0):
        print("Solução não encontrada")
        return
    print("Solução encontrada:")
    imprimir_tabuleiro()

def main():
    resolver_nq()

if __name__ == "__main__":
    main()
