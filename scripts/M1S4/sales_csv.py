import csv

def main():
    vendas = {}
    with open('data/input/csv/vendas.csv', 'r', encoding='UTF-8') as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            produto, quantidade, valor = line
            vendas[produto] = {'quantidade': quantidade, 'valor': valor}
    
    with open('data/output/csv/total_vendas.csv', 'w', encoding='UTF-8', newline='') as newfile:
        writer = csv.writer(newfile)
        writer.writerow(['produto', 'quantidade', 'valor', 'total'])
        for produto in vendas:
            quantidade = int(vendas[produto]['quantidade'])
            valor = float(vendas[produto]['valor'])
            total = quantidade * valor
            writer.writerow([produto, quantidade, valor, round(total, 2)])

if __name__ == "__main__":
    main()