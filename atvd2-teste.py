import random
def gerar_numeros_aleatorios(qtd=20000, menor=-999999, maior=999999):
    return [random.randint(menor, maior) for _ in range(qtd)]

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

def testar_ordenacao():
    lista_numeros = gerar_numeros_aleatorios()
    
    lista_ordenada = quicksort(lista_numeros)
    
    for i in range(len(lista_ordenada) - 1):
        assert lista_ordenada[i] <= lista_ordenada[i + 1], f"Erro na ordenação entre {lista_ordenada[i]} e {lista_ordenada[i+1]}"
    
    print("Ordenação correta e todos os testes passaram!")

testar_ordenacao()
