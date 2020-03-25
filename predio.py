
class Predio():
	def __init__(self):
		self.qtd_de_salas_por_andar = 8
		self.quantidade_de_andares = 100 
		self.quantidade_total = self.qtd_de_salas_por_andar * self.quantidade_de_andares
		self.salas = []
		self.nuber_terrio = 400

	def cadastro_sala(self, andar, numero):
		self.salas.append([andar, numero])

	def find_by_andar(self, numero):
		query = [i for i in self.salas if i[0]==numero ][0]
		return query

	def find_by_sala(self, numero):
		query = [i for i in self.salas if i[1]==numero ][0]
		return query

predio = Predio()
predio.cadastro_sala(100, 321)
predio.cadastro_sala(100, 322)
predio.cadastro_sala(100, 323)
predio.cadastro_sala(100, 324)

sala = predio.find_by_sala(322)
print("Andar: ", sala[0])
print("Sala: ", sala[1])
