nomes = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo', 'Fernanda', 'Gustavo', 'Helena']
idades = [23, 35, 19, 42, 28, 31, 27, 40]

def main():
    registro = {}
    
    for i in range(len(nomes)):
        registro[nomes[i]] = idades[i]

    print(registro)

if __name__ == "__main__":
    main()
