import os
import json
from graphviz import Digraph

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

people = {}

def save():
	p = {}
	for i in people.keys():
		p[i] = people[i].__dict__
	print(p)
	with open('tree.txt', 'w') as f:
		f.write(json.dumps(p))

def load():
	with open('tree.txt', 'r') as f:
		jl = f.read()
		p = json.loads(jl)
	people = {}
	for i in p.keys():
		person = Person(i)
		person.__dict__ = p[i]
		people[i] = person
	return people

def plot():
	
	c = 65
	peeps = {}
	edges = []
	dot = Digraph()
	
	for i in people.keys():
		
		if i not in peeps.keys(): 
			peeps[i] = chr(c)
			c+=1
		dot.node(p[i], i)
		
		if people[i].spouse != None:
			if people[i].spouse not in peeps.keys(): 
				peeps[people[i].spouse] = chr(c)
				c += 1
			edges.append(peeps[i] + peeps[people[i].spouse])
		
		if len(people[i].parents) > 0:
			for j in people[i].parents:
				edges.append(people[i].name + j)

	print(dot.source)
	print(edges)
	dot.edges = (edges)
	dot.render('test-output/familyTree.gv', view=True)

if __name__ == "__main__":
	# Load
	while(1):
		print("1- Load\n2- Save\n3- Add Person\n4- Add Relation\n5- Plot\n6- Exit\n")
		choice = input()
		os.system('clear')
		if choice == '1':
			people = load()
		elif choice == '2':
			save()
		elif choice == '3':
			print("Enter Name:", end=" ")
			name = input()
			if name not in people.keys():
				p = Person(name)
				people[name] = p
		elif choice == '4':
			print("Add relation to:", end=" ")
			name = input()
			print("Relative Name:", end=" ")
			relative = input()
			person = people[name]
			print("1- Add Parent\n2- Add Sibling\n3- Add Child\n4- Add Spouse\n5- Exit\n")
			choice = input()
			os.system('clear')
			if choice == '1':
				people[name].addParent(relative)
				people[relative].addChild(name)
			elif choice == '2':
				people[name].addSibling(relative)
				people[relative].addSibling(name)
			elif choice == '3':
				people[name].addChild(relative)
				people[relative].addParent(name)
			elif choice == '4':
				people[name].addSpouse(relative)
				people[relative].addSpouse(name)
		elif choice == '5':
			plot()
		elif choice == '6':
			break
		print(people)