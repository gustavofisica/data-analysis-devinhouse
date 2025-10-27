from calculations import soma, subtracao, divisao, multiplicacao, potenciacao, modulo
from dates import diferenca_dias, adicionar_dias, eh_final_de_semana, str_para_data, data_para_str

def menu():
	print("Escolha uma operação:")
	print("1 - Soma")
	print("2 - Subtração")
	print("3 - Divisão")
	print("4 - Multiplicação")
	print("5 - Potenciação")
	print("6 - Módulo")
	print("7 - Diferença de dias entre datas")
	print("8 - Adicionar dias a uma data")
	print("9 - Verificar se data é final de semana")
	print("0 - Sair")

def main():
	while True:
		menu()
		opcao = input("Opção: ")
		if opcao == '0':
			print("Saindo...")
			break
		elif opcao in ['1','2','3','4','5','6']:
			a = float(input("Digite o primeiro valor: "))
			b = float(input("Digite o segundo valor: "))
			if opcao == '1':
				print("Resultado:", soma(a, b))
			elif opcao == '2':
				print("Resultado:", subtracao(a, b))
			elif opcao == '3':
				if b == 0:
					print("Erro: divisão por zero!")
				else:
					print("Resultado:", divisao(a, b))
			elif opcao == '4':
				print("Resultado:", multiplicacao(a, b))
			elif opcao == '5':
				print("Resultado:", potenciacao(a, b))
			elif opcao == '6':
				print("Resultado:", modulo(a, b))
		elif opcao == '7':
			data1 = input("Digite a primeira data (dd/mm/aaaa): ")
			data2 = input("Digite a segunda data (dd/mm/aaaa): ")
			d1 = str_para_data(data1)
			d2 = str_para_data(data2)
			print("Diferença em dias:", diferenca_dias(d1, d2))
		elif opcao == '8':
			data = input("Digite a data (dd/mm/aaaa): ")
			dias = int(input("Quantos dias adicionar? "))
			d = str_para_data(data)
			nova_data = adicionar_dias(d, dias)
			print("Nova data:", data_para_str(nova_data))
		elif opcao == '9':
			data = input("Digite a data (dd/mm/aaaa): ")
			d = str_para_data(data)
			if eh_final_de_semana(d):
				print("É final de semana.")
			else:
				print("Não é final de semana.")
		else:
			print("Opção inválida!")

if __name__ == "__main__":
	main()
