def media_lista(lista: list) -> float:
    """
    Calcula a média dos valores de uma lista.

    Parâmetros:
        lista (list): Lista de números.

    Retorna:
        float: Média dos valores da lista.
    """
    return sum(lista) / len(lista)

def max_min_lista(lista: list) -> list:
    """
    Retorna o maior e o menor valor de uma lista.

    Parâmetros:
        lista (list): Lista de números.

    Retorna:
        list: Lista contendo o maior e o menor valor, respectivamente.
    """
    max_item = max(lista)
    min_item = min(lista)
    return [max_item, min_item]

# lista de valores de entrada
lista = [10, 20, 30, 40, 50, 60, 70, 90]

def main():
    media = media_lista(lista)
    max_valor, min_valor = max_min_lista(lista)
    print(f'A média dos valores da lista é {media}')
    print(f'O valor máximo da lista é {max_valor} e o valor mínimo é {min_valor}')

if __name__ == "__main__":
    main()
