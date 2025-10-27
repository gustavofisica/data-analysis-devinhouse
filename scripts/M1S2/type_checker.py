def verificar_tipo(valor_str):
    '''
    Verifica o tipo de dado da entrada do usuário.

    Parâmetros:
        valor_str (str): Valor digitado pelo usuário.

    Retorna:
        str: 'int' se for inteiro, 'float' se for decimal, 'str' se for texto.
        Se for booleano, retorna erro de não enquadramento.
    '''
    if valor_str.lower() in ['true', 'false']:
        print(f'Erro: valor booleano não é permitido para este exercício.')
        return 'erro'
    try:
        valor_int = int(valor_str)
        print(f'Você digitou um número inteiro: {valor_int}')
        return 'int'
    except ValueError:
        try:
            valor_float = float(valor_str)
            print(f'Você digitou um número decimal: {valor_float}')
            return 'float'
        except ValueError:
            print(f'Você digitou uma string: "{valor_str}"')
            return 'str'

def main():
    while True:
        valor = input("Digite um valor: ")
        verificar_tipo(valor)
        continuar = input("Deseja testar outro valor? (s/n): ").strip().lower()
        if continuar != 's':
            print("Programa encerrado.")
            break

if __name__ == "__main__":
    main()
