preco_produtos = {
    'arroz': 8.99,
    'feijao': 7.49,
    'macarrao': 4.50,
    'oleo': 6.25,
    'acucar': 3.99,
    'leite': 5.20,
    'pao': 2.50,
    'manteiga': 9.30,
    'sal': 1.75,
    'farinha': 4.10,
    'cafe': 18.90,
    'suco': 6.50,
    'cafeteira': 249.90,
    'microondas': 399.90,
    'aspirador': 499.00,
    'geladeira': 2499.90,
    'televisao': 1599.00,
    'notebook': 3499.00,
    'smartphone': 1999.99,
    'moedor': 129.50,
    'liquidificador': 179.90
}

def main():
    print('Relação de produtos acima de R$ 100,00')
    for produto, preco in preco_produtos.items():
        if preco > 100.00:
            print(f'O produto: {produto}, está com o preço de R$ {preco:.2f}')


if __name__ == "__main__":
    main()