class student():
	def __init__(self,name,age,fen):
		self.nam1 = name
		self.age1 = age
		self.fen1 = fen
	def name(self):
		print(str(self.nam1))
	def age(self):
		print(int(self.age1))
	def fen(self):
		print(max(self.fen1))

a = str(input('name:'))
b = input('age:')
c=eval(input('course:'))
xm = student(a,b,c)
xm.name()
xm.age()
xm.fen()
