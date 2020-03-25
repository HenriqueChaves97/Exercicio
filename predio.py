
class Predio():
	def __init__(self):
		#quantidade de sala por andares
		self.qtd_SPA = 8
		#quantidade de andares
		self.qtd_andares = 100 
		self.qtd_total_de_salas = self.qtd_SPA * self.qtd_andares
		self.salas = []

	def cadastro_sala(self, numero):
		andar = self.qtd_andares -(((self.qtd_andares*self.qtd_SPA)-numero)/self.qtd_SPA)
		self.salas.append([andar, numero])

	def find_by_andar(self, numero):
		try:
			query = [i for i in self.salas if i[0]==numero ][0]
			return query
		except:
			return ["Andar não encontrado!", None]

	def find_by_sala(self, numero):
		try:
			query = [i for i in self.salas if i[1]==numero ][0]
			return query
		except:
			return [None, "Nenhuma encontrada!"]
		

predio = Predio()
predio.cadastro_sala(7)
predio.cadastro_sala(9)
predio.cadastro_sala(323)
predio.cadastro_sala(1)
predio.cadastro_sala(700)

sala1 = predio.find_by_sala(9)
sala2 = predio.find_by_sala(324)
sala3 = predio.find_by_sala(7)
sala4 = predio.find_by_sala(700)

print("Andar: ", sala1 [0])
print("Sala: ", sala1 [1])
