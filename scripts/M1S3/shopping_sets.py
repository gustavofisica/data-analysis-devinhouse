compras_joao = ['arroz', 'feijão', 'macarrão', 'leite', 'pão', 'café', 'azeite', 'biscoito']
compras_maria = ['arroz', 'feijão', 'leite', 'pão', 'suco', 'manteiga', 'biscoito', 'chocolate']

def main():
    conjunto_compras_joao = set(compras_joao)
    conjunto_compras_maria = set(compras_maria)

    print(f'Itens comuns nas compras de João e Maria são: {conjunto_compras_joao.intersection(conjunto_compras_maria)}')
    print(f'Itens exclusivos nas listas de compras de João e Maria são: {conjunto_compras_joao.symmetric_difference(conjunto_compras_maria)}')
    print(f'As listas de compras de João e Maria têm os seguintes itens: {conjunto_compras_joao.union(conjunto_compras_maria)}')

if __name__ == "__main__":
    main()
