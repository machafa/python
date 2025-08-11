

class Person:
	amount=0

	#here we define a function that gets data, stores it and then gives #it to a specific variableS
	#acrescentamos pessoas usando metodos simples tipo de java de soma e de classe. Uma classe eh que nem um vector 
	def __init__(self,name,age,height):
		self.name=name
		self.age=age
		self.height=height
		Person.amount +=1 #contamos dados que temos atraves de Person porque eh "tabela" enquanto self eh "record"
		
		
	def __del__(self):
		Person.amount -=1 #para apagar record
		
		
#essa funcao eh tipo de java. deve retornar algo e recicla person1 #colocando info que quero em linha tipo vector
	def __str__(self):
		return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)
		
		
#here we give the info to the class that works with the function to later #print the necessary

person1=Person("Maura",15,170)
person2=Person("Penelope",25,180)
del person2
print(Person.amount)
