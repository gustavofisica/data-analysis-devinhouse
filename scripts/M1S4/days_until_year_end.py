from datetime import datetime

final_ano = datetime.strptime('31/12/2025', "%d/%m/%Y")
dias_semana = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira', 'sábado', 'domingo']

def main():
    while True:
        data_atual = input("Digite a data atual no formato dd/mm/aaaa: ")
        try:
            data_atual = datetime.strptime(data_atual, "%d/%m/%Y")
            break
        except ValueError:
            print("Formato inválido! Tente novamente (ex: 16/10/2025).")

    print(f'Faltam {(final_ano - data_atual).days} dias para o final do ano.')
    print(f'Hoje é {dias_semana[data_atual.weekday()]}.')

if __name__ == "__main__":
    main()