QTD_NOTAS = 3
notas_alunos = {}

def cadastrar_aluno(qtd_alunos):
    """
    Cadastra alunos e suas notas em um dicionário.
    """
    for i in range(qtd_alunos):
        nome = input("Digite o nome do aluno: ").strip().capitalize()
        notas = []
        for i in range(QTD_NOTAS):
            while True:
                try:
                    nota = float(input(f'Digite a {i+1}° nota (0 - 10): '))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Nota inválida! Digite um valor entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida! Digite um número.")
        notas_alunos[nome] = notas


def calcular_media(notas: list):
    """
    Calcula a média aritmética dos valores em uma lista de notas.

    Parâmetros:
        notas (list): Lista de números (notas) do aluno.

    Retorna:
        float: Média aritmética das notas.
    """

    return sum(notas) / len(notas)

def main():
    while True:
        try:
            qtd_alunos = int(input("Digite quantos alunos deseja cadastrar: "))
            if qtd_alunos > 0:
                break
            else:
                print("Digite um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

    cadastrar_aluno(qtd_alunos)

    for aluno, notas in notas_alunos.items():
        media = calcular_media(notas)
        if media >= 7.0:
            print(f'Aluno: {aluno}  |   Média: {round(media, 2)}  |   Situação: APROVADO')
        else:
            print(f'Aluno: {aluno}  |   Média: {round(media, 2)}  |   Situação: REPROVADO')
        
if __name__ == "__main__":
    main()
