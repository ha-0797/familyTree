class Person(object):
	"""docstring for Person"""
	def __init__(self, name):
		super(Person, self).__init__()
		self.name 		= name
		self.parents 	= []
		self.children	= []
		self.spouse		= None

	def addParent(self, P):
		self.parents.append(P)

	def addChild(self, C):
		self.children.append(C)

	def addSpouse(self, S):
		self.spouse = S