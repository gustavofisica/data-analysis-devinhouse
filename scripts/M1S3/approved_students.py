notas_fisica = {
    'Maria': [5.5, 7.8, 10.0],
    'João': [6.0, 6.5, 7.0],
    'Ana': [9.5, 8.0, 7.5],
    'Carlos': [4.0, 5.5, 6.0],
    'Beatriz': [7.0, 7.5, 8.0],
}

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
    print('Os aprovados na disciplina de física são:')
    for aluno, notas in notas_fisica.items():
        media = calcular_media(notas)
        if media >= 7.0:
            print(f'Aluno: {aluno} com média: {media:.2f}')
   

if __name__ == "__main__":
    main()
