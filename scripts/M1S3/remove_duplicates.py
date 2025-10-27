numeros = [1, 2, 5, 7, 2, 8, 5, 10, 12, 7, 15, 20, 15, 8]

def main():
    conjunto_numeros = set(numeros)
    print(f'Lista de números original: {numeros}')
    print('Removendo duplicatas da lista...')
    print(f'Conjunto de números únicos: {conjunto_numeros}')


if __name__ == "__main__":
    main()
