# -*- coding: UTF-8 -*-

class Data(object):
	"Classe de data"

	def __init__(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def imprimir(self):
		print("Dia %s do %s de %s" % (self.dia, self.mes, self.ano))
