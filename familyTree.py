import os
import json
from graphviz import Digraph
import tkinter as tk
from person import Person

people = {}

def save():
	p = {}
	for i in people.keys():
		p[i] = people[i].__dict__
	print(p)
	with open('tree.txt', 'w') as f:
		f.write(json.dumps(p))

def load():
	global people
	with open('tree.txt', 'r') as f:
		jl = f.read()
		p = json.loads(jl)
	for i in p.keys():
		person = Person(i)
		person.__dict__ = p[i]
		people[i] = person

def plot():
	
	c = 65
	peeps = {}
	edges = []
	dot = Digraph(name='Family-Tree', node_attr={'shape': 'plaintext'})
	
	for i in people.keys():
		dot.attr('node', shape='egg')
		if i not in peeps.keys(): 
			dot.node(i)
		
		if len(people[i].children) > 0:
			for j in people[i].children:
				dot.edge(people[i].name, j)

	print(dot.source)
	print(edges)
	# dot.edges(edges)
	dot.render('test-output/familyTree.gv', view=True)

class add(object):
	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)
        
		self.label1 = tk.Label(self.frame, text="Name")
		self.box1 = tk.Entry(self.frame)
		self.label2 = tk.Label(self.frame, text="Parent 1")
		self.box2 = tk.Entry(self.frame)
		self.label3 = tk.Label(self.frame, text="Parent 2")
		self.box3 = tk.Entry(self.frame)
		self.button = tk.Button(self.frame, text= "Submit", command= self.submit)

		self.label1.pack()
		self.box1.pack()
		self.label2.pack()
		self.box2.pack()
		self.label3.pack()
		self.box3.pack()
		self.button.pack()
		self.frame.pack()

	def submit(self):
		global people
		name = self.box1.get()
		if name not in people.keys():
			newPerson = Person(name)
			people[name] = newPerson
			parent1 = self.box2.get()
			parent2 = self.box3.get()
			if parent1 != '' and parent2 != '':
				newPerson.addParent(parent1)
				newPerson.addParent(parent2)
				people[parent1].addChild(Name)
				people[parent2].addChild(name)
		self.master.destroy()

class mainWindow(object):
	def __init__(self, master):
		self.master = master
		self.frame = tk.Frame(self.master)
		self.button1 = tk.Button(self.frame, text = 'Load', width = 25, command = load)
		self.button2 = tk.Button(self.frame, text = 'Save', width = 25, command = save)
		self.button3 = tk.Button(self.frame, text = 'Add Person', width = 25, command = self.new_window)
		self.button4 = tk.Button(self.frame, text = 'Plot', width = 25, command = plot)        
		self.button5 = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)        
		self.button1.pack()
		self.button2.pack()
		self.button3.pack()
		self.button4.pack()
		self.button5.pack()
		self.frame.pack()

	def new_window(self):
		self.newWindow = tk.Toplevel(self.master)
		self.app = add(self.newWindow)

	def close_windows(self):
		self.master.destroy()

if __name__ == "__main__":

	root = tk.Tk()
	app = mainWindow(root)
	root.mainloop()