#coding:UTF-8 
class User(object):

	def __init__(self, name, email, password):
		self._validated_email(email)
		self._validated_password(password)
		self.name = name
		self.email = email
		self.password = password


	def update_email(self, new_email):
		self._validated_email(new_email)
		self.email = new_email
#validação de email usando in precisa ter @ e .

	def _validated_email(self, email):
		if not email or not email.strip():
			raise ValueError('campo de email vazio')

		if '@' not in email or '.' not in email or '.@' in email or '@.' in email:
			raise ValueError('email invalido')		

	def _validated_password(self, password):
		if len(password) < 8 :
			raise ValueError('senha deve ter mais que 8 caracteres')

		if password.isupper() == False:
			raise ValueError('senha precisa ter no minímo um caracter maiusculo')

		#não fazer sa caralha
		if password.upper() not in password:
			raise ValueError('senha precisa ter no minímo um caracter maiusculo')
				
		
		
