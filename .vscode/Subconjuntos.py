# Passo 1: Construindo um algoritmo para encontrar um subconjunto cuja soma seja zero

# Função para encontrar subconjuntos que somam zero
def encontra_subconjunto_zero(nums):
    # Itera sobre todos os possíveis subconjuntos (usando bits para representar subconjuntos)
    for i in range(1, 1 << len(nums)):
        subset = []
        # Constrói um subconjunto baseado na representação binária do número
        for j in range(len(nums)):
            if i & (1 << j):
                subset.append(nums[j])
        # Verifica se a soma do subconjunto é zero
        if sum(subset) == 0:
            return subset
    return None

# Passo 2: Implementando o algoritmo em Python

# Função de teste para validar o algoritmo
def testa_algoritmo():
    exemplos = [
        [-7, -3, -2, 5, 8],
        [1, 2, 3, 4, 5],
        [0, 1, -1],
        [1, -1, 2, -2, 3, -3]
    ]
    for nums in exemplos:
        resultado = encontra_subconjunto_zero(nums)
        print(f"Conjunto: {nums}")
        print(f"Subconjunto que soma zero: {resultado}")
        print("-" * 30)

# Testando o algoritmo
testa_algoritmo()

# Passo 3: Modificando o código para mostrar cada passo

# Função para encontrar subconjuntos que somam zero e mostrar os passos
def encontra_subconjunto_zero_com_passos(nums):
    for i in range(1, 1 << len(nums)):
        subset = []
        for j in range(len(nums)):
            if i & (1 << j):
                subset.append(nums[j])
        # Mostra o subconjunto e sua soma
        print(f"Subconjunto: {subset}, Soma: {sum(subset)}")
        if sum(subset) == 0:
            return subset
    return None

# Função de teste para validar o algoritmo e mostrar os passos
def testa_algoritmo_com_passos():
    exemplos = [
        [-7, -3, -2, 5, 8],
        [1, 2, 3, 4, 5],
        [0, 1, -1],
        [1, -1, 2, -2, 3, -3]
    ]
    for nums in exemplos:
        print(f"Conjunto: {nums}")
        resultado = encontra_subconjunto_zero_com_passos(nums)
        print(f"Subconjunto que soma zero: {resultado}")
        print("-" * 30)

# Testando o algoritmo com passos
testa_algoritmo_com_passos()