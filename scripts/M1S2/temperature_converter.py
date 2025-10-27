def conversor_temperatura(valor:float, da_unidade:str = 'C', para_unidade:str = 'F') -> float:
    ''''
    Converte um valor de temperatura de uma unidade para outra. 
    Valores de unidades aceitas são: "C" para Celsius, "F" para Fahrenheit  e "K" para Kelvin.
    Parâmetros:
    valor (float): O valor da temperatura a ser convertido.
    da_unidade (str): A unidade de medida da temperatura de entrada.
    para_unidade (str): A unidade de medida da temperatura de saída.
    Retorna: float: O valor convertido.
    '''
    
    try:
        if da_unidade.upper().strip() == 'C' and para_unidade.upper().strip() == 'F':
            return (valor * 9/5) + 32
        elif da_unidade.upper().strip() == 'C' and para_unidade.upper().strip() == 'K':
            return valor + 273.15
        elif da_unidade.upper().strip() == 'F' and para_unidade.upper().strip() == 'C':
            return (valor - 32) * 5/9
        elif da_unidade.upper().strip() == 'F' and para_unidade.upper().strip() == 'K':
            return ((valor - 32) * 5/9) + 273.15
        elif da_unidade.upper().strip() == 'K' and para_unidade.upper().strip() == 'C':
            return valor - 273.15
        elif da_unidade.upper().strip() == 'K' and para_unidade.upper().strip() == 'F':
            return ((valor - 273.15) * 9/5) + 32
        else:
            raise ValueError("Unidade de medida inválida.")
    except Exception as e:
        print(f'Erro: {e}')
        return None

def main():
    while True:
        valor = float(input("Digite o valor que deseja converter: "))

        print("Para as unidades a seguir, digite 'C' para Celsius, 'F' para Fahrenheit ou 'K' para Kelvin.")
        da_unidade = input("Esse valor está em C, F ou K? ").upper()
        para_unidade = input("Você deseja converter para C, F ou K? ").upper()

        print(f'Convertendo {valor} de °{da_unidade} para °{para_unidade}...')
        print('-' * 10)

        valor_convertido = conversor_temperatura(valor=valor, da_unidade=da_unidade, para_unidade=para_unidade)

        if valor_convertido is not None:
            if da_unidade == 'C' or da_unidade == 'F':
                da_unidade = f'°{da_unidade}'
            if para_unidade == 'C' or para_unidade == 'F':
                para_unidade = f'°{para_unidade}'

            print(f'O valor {valor} em {da_unidade} fica {valor_convertido:.2f} em {para_unidade}')

            continuar = input("Deseja fazer outra conversão? (s/n): ").strip().lower()
            if continuar != 's':
                print("Programa encerrado.")
                break
        else:
            print("Conversão não realizada. Verifique as unidades informadas.")
            continue

if __name__ == "__main__":
    main()
