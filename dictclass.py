#输入字典时字母为什么必须有引号。

class dictclass():
	def __init__(self,dic):
		self.dic1=dic
	def rmdic(self,key1):
		self.dic1.pop(key1)
		print(self.dic1)
	def find(self,key2):
		print(self.dic1[key2]) if key2 in self.dic1 else print('not found')
	def key_list(self):
		print('键的列表{}'.format(list(self.dic1.keys())))
	def update(self,dict2):
		a = list(dict2.items())
		b= list(self.dic1.items())
		dic3 = dict(a+b)		
		print('合并后values值{}'.format(list(dic3.values())))
dic = eval(input('字典：'))
dict0 = dictclass(dic)
key1 = input('如删除输入key，不删除输入no：')
if key1=='no':
	pass
else:
	dict0.rmdic(eval(key1))
key2 = input('如查找输入key，不查找输入no：')
if key2=='no':
	pass
else:
	dict0.find(eval(key2))
dict0.key_list()
key3 = input('如合并入字典，不合并输入no：')
if key3=='no':
	pass
else:
	dict0.update(eval(key3))


