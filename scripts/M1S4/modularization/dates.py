from datetime import datetime, timedelta

def diferenca_dias(data1: datetime, data2: datetime) -> int:
	"""
	Retorna a diferença em dias entre duas datas.
	"""
	return abs((data2 - data1).days)

def adicionar_dias(data: datetime, dias: int) -> datetime:
	"""
	Retorna uma nova data somando a quantidade de dias à data informada.
	"""
	return data + timedelta(days=dias)

def eh_final_de_semana(data: datetime) -> bool:
	"""
	Verifica se a data é sábado ou domingo.
	"""
	return data.weekday() >= 5

def str_para_data(data_str: str, formato: str = "%d/%m/%Y") -> datetime:
	"""
	Converte uma string para um objeto datetime.
	"""
	return datetime.strptime(data_str, formato)

def data_para_str(data: datetime, formato: str = "%d/%m/%Y") -> str:
	"""
	Converte um objeto datetime para string no formato desejado.
	"""
	return data.strftime(formato)
