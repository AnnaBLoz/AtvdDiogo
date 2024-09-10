import random

def gerar_numeros_aleatorios(qtd=20000, menor=-999999, maior=999999):
    """Gera uma lista de valores inteiros aleatórios."""
    return [random.randint(menor, maior) for _ in range(qtd)]

def testar_gerar_numeros_aleatorios():
    lista_numeros = gerar_numeros_aleatorios()
    
    assert len(lista_numeros) == 20000, f"Tamanho da lista incorreto: {len(lista_numeros)}"

    for numero in lista_numeros:
        assert -999999 <= numero <= 999999, f"Valor fora do intervalo: {numero}"

    print("Todos os testes passaram!")

testar_gerar_numeros_aleatorios()
