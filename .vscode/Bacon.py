class Ator:
    def __init__(self, nome):
        self.nome = nome
        self.filmes = set()  # Conjunto de filmes em que o ator participou

class Filme:
    def __init__(self, titulo):
        self.titulo = titulo
        self.atores = set()  # Conjunto de atores que participaram do filme

# Função para adicionar um ator a um filme
def adicionar_ator_ao_filme(ator, filme):
    ator.filmes.add(filme)
    filme.atores.add(ator)

# Função para encontrar o Número de Bacon entre dois atores
def encontrar_numero_de_bacon(ator1, ator2):
    if ator1 == ator2:
        return 0  # Se os atores forem os mesmos, o número de Bacon é 0

    # Fila para a busca em largura (BFS)
    fila = [(ator1, 0)]
    visitados = set()  # Conjunto de atores já visitados
    visitados.add(ator1)

    while fila:
        ator_atual, numero_de_bacon = fila.pop(0)

        # Itera sobre os filmes em que o ator atual participou
        for filme in ator_atual.filmes:
            # Itera sobre os atores que participaram do mesmo filme
            for co_ator in filme.atores:
                if co_ator == ator2:
                    return numero_de_bacon + 1  # Se encontramos o ator alvo, retornamos o número de Bacon
                if co_ator not in visitados:
                    visitados.add(co_ator)
                    fila.append((co_ator, numero_de_bacon + 1))

    return -1  # Se não encontramos uma conexão, retornamos -1

# Função para encontrar o caminho de filmes entre dois atores
def encontrar_caminho_de_bacon(ator1, ator2):
    if ator1 == ator2:
        return (0, [])  # Se os atores forem os mesmos, o número de Bacon é 0 e o caminho é vazio

    # Fila para a busca em largura (BFS)
    fila = [(ator1, 0, [])]
    visitados = set()
    visitados.add(ator1)

    while fila:
        ator_atual, numero_de_bacon, caminho = fila.pop(0)

        # Itera sobre os filmes em que o ator atual participou
        for filme in ator_atual.filmes:
            novo_caminho = caminho[:]
            novo_caminho.append(filme.titulo)

            # Itera sobre os atores que participaram do mesmo filme
            for co_ator in filme.atores:
                if co_ator == ator2:
                    return (numero_de_bacon + 1, novo_caminho)  # Se encontramos o ator alvo, retornamos o número de Bacon e o caminho
                if co_ator not in visitados:
                    visitados.add(co_ator)
                    fila.append((co_ator, numero_de_bacon + 1, novo_caminho))

    return (-1, [])  # Se não encontramos uma conexão, retornamos -1 e um caminho vazio

# Base de dados simulada
atores = {
    "Kevin Bacon": Ator("Kevin Bacon"),
    "Tom Hanks": Ator("Tom Hanks"),
    "Bill Paxton": Ator("Bill Paxton")
}

filmes = {
    "Apollo 13": Filme("Apollo 13"),
    "Toy Story": Filme("Toy Story")
}

# Adicionando atores aos filmes
adicionar_ator_ao_filme(atores["Kevin Bacon"], filmes["Apollo 13"])
adicionar_ator_ao_filme(atores["Tom Hanks"], filmes["Apollo 13"])
adicionar_ator_ao_filme(atores["Bill Paxton"], filmes["Apollo 13"])
adicionar_ator_ao_filme(atores["Tom Hanks"], filmes["Toy Story"])

# Encontrando o Número de Bacon entre Kevin Bacon e Tom Hanks
print(f"Número de Bacon: {encontrar_numero_de_bacon(atores['Kevin Bacon'], atores['Tom Hanks'])}")  # Saída: 1

# Encontrando o caminho de filmes entre Kevin Bacon e Tom Hanks
numero_de_bacon, caminho = encontrar_caminho_de_bacon(atores["Kevin Bacon"], atores["Tom Hanks"])
print(f"Número de Bacon: {numero_de_bacon}")
print(f"Caminho: {' -> '.join(caminho)}")  # Saída: "Apollo 13"
