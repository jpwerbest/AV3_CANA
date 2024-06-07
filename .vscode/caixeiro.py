import os

def permutar(cidades):
    if len(cidades) <= 1:
        return [cidades]

    permutacoes = []
    stack = [(list(cidades), 0)]

    while stack:
        cidades_atuais, nivel = stack.pop()

        if nivel == len(cidades_atuais) - 1:
            permutacoes.append(cidades_atuais)

        for i in range(nivel, len(cidades_atuais)):
            cidades_permutadas = cidades_atuais[:]
            cidades_permutadas[nivel], cidades_permutadas[i] = cidades_permutadas[i], cidades_permutadas[nivel]
            stack.append((cidades_permutadas, nivel + 1))

    return permutacoes

def calcular_distancia(cidades, rota):
    distancia_total = 0
    n = len(rota)
    for i in range(n - 1):
        cidade_atual = rota[i]
        proxima_cidade = rota[i + 1]
        distancia_total += cidades[cidade_atual][proxima_cidade]
    distancia_total += cidades[rota[-1]][rota[0]]
    return distancia_total

def caixeiro_viajante(cidades):
    cidades_indices = list(cidades.keys())
    melhor_rota = None
    menor_distancia = float('inf')
    permutacoes = permutar(cidades_indices)

    rotas_para_printar = []
    for rota in permutacoes:
        rota.append(rota[0])
        rotas_para_printar.append(rota)

        distancia = calcular_distancia(cidades, rota)
        if distancia < menor_distancia:
            menor_distancia = distancia
            melhor_rota = rota

    print("Melhor rota:", melhor_rota)
    print("Menor distância:", menor_distancia, "\n")

    def print_rotas(rotas, per_page=10):
        total_rotas = len(rotas)
        for i in range(0, total_rotas, per_page):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Mostrando rotas {i+1} a {min(i+per_page, total_rotas)} de {total_rotas}")
            for rota in rotas[i:i+per_page]:
                print(rota)
            if i + per_page < total_rotas:
                input("Pressione Enter para ver mais rotas...\n")
            else:
                print("Fim das rotas.")

    print_rotas(rotas_para_printar)

cidades = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20, 'E': 25, 'F': 30, 'G': 35, 'H': 40, 'I': 45, 'J': 50},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25, 'E': 30, 'F': 20, 'G': 45, 'H': 25, 'I': 30, 'J': 35},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30, 'E': 40, 'F': 25, 'G': 50, 'H': 40, 'I': 35, 'J': 20},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0, 'E': 35, 'F': 30, 'G': 25, 'H': 20, 'I': 15, 'J': 10},
    'E': {'A': 25, 'B': 30, 'C': 40, 'D': 35, 'E': 0, 'F': 45, 'G': 20, 'H': 25, 'I': 30, 'J': 35},
    'F': {'A': 30, 'B': 20, 'C': 25, 'D': 30, 'E': 45, 'F': 0, 'G': 35, 'H': 40, 'I': 25, 'J': 30},
    'G': {'A': 35, 'B': 45, 'C': 50, 'D': 25, 'E': 20, 'F': 35, 'G': 0, 'H': 15, 'I': 30, 'J': 25},
    'H': {'A': 40, 'B': 25, 'C': 40, 'D': 20, 'E': 25, 'F': 40, 'G': 15, 'H': 0, 'I': 35, 'J': 30},
    'I': {'A': 45, 'B': 30, 'C': 35, 'D': 15, 'E': 30, 'F': 25, 'G': 30, 'H': 35, 'I': 0, 'J': 20},
    'J': {'A': 50, 'B': 35, 'C': 20, 'D': 10, 'E': 35, 'F': 30, 'G': 25, 'H': 30, 'I': 20, 'J': 0}
}
caixeiro_viajante(cidades)