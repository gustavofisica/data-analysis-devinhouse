import re

emails = [
	'joao@gmail.com',
	'maria.silva@empresa.com.br',
	'usuario123@yahoo.com',
	'email.invalido@',
	'semarroba.com',
	'ana@dominio',
	'carlos@site.com',
	'teste@teste',
	'lucas@outlook.com',
	'invalido@.com',
]

regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
emails_validos = []
emails_invalidos = []

def gerar_arquivo_emails(nome_arquivo: str, lista_emails: list):
    """
    Gera um arquivo texto contendo cada item da lista em uma linha.

    Parâmetros:
    nome_arquivo (str): Nome do arquivo a ser criado.
    lista (list): Lista de strings a serem escritas no arquivo.
    """
    with open(nome_arquivo, 'w', encoding='UTF-8') as file:
        for email in lista_emails:
            file.write(f'{email}\n')

def main():
    for email in emails:
        if re.fullmatch(regex, email):
            emails_validos.append(email)
        else:
            emails_invalidos.append(email)
    gerar_arquivo_emails('data/emails_validos.txt', emails_validos)
    gerar_arquivo_emails('data/emails_invalidos.txt', emails_invalidos)

if __name__ == "__main__":
    main()