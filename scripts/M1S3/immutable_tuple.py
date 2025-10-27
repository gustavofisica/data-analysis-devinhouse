tupla = ('o', 'meu', 'nome', 'é', 'Pedro')

def main():
    # Tentativa de atribuição 
    tupla[-1] = 'Carlos'
    """
    Essa operação gera um erro de tipo, pois o objeto tupla é imutável, ou seja,
    seus elementos não podem ser alterados. Para alterar, precisamos fazer uma 
    modficação de objeto, assim:
    """
    lista = list(tupla)
    lista[-1] = 'Carlos'
    print(lista)

if __name__ == "__main__":
    main()
