# -*- coding: UTF-8 -*-

class Pessoa(object):
	"Calculo do IMC"

	def __init__(self, pessoa, peso, altura):
		self.pessoa = pessoa
		self.peso = float(peso)
		self.altura = float(altura)

	def imprime_imc(self):
		imc = self.peso / (self.altura **2)
		print "O Imc de %s é: %s" %(self.pessoa, imc)
