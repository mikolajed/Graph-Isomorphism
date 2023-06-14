from itertools import permutations

class Tree:
	def __init__(self, n, m, root=0, edges=[]):
		self.root = root
		self.num_nodes = n
		self.num_edges = m
		self.graph = []
		# if not a tree
		if (m != n-1):
			exit(0)

		self.graph = [[] for _ in range(self.num_nodes)]
		for edge in edges:
			u, v = edge
			self.graph[u].append(v)
	
	def print_graph(self):
		for i, adj_list in enumerate(self.graph):
			print(f"Node {i}: {adj_list}")

def isomorphic(G, H):
	visited_G = [0] * G.num_nodes
	visited_H = [0] * H.num_nodes
	# nodes of one layer in G
	layer_G = []
	# find leafes and append them onto the stack
	for i in range(G.num_nodes):
		if (len(G.graph[i]) == 1):
			layer_G.append(i)
			visited_G[i] = 1
	# nodes of one layer in H
	layer_H = []
	# find leafes and append them onto the stack
	for i in range(H.num_nodes):
		if (len(H.graph[i]) == 1):
			layer_H.append(i)
			visited_H[i] = 1

	# dictionary with a pair id number and a set representing set of id of a children nodes
	indexes = dict()
	# initial index - used to indentify leafes
	idx = 0
	# store a pair node number and its index in indexes dict
	ids_G = dict()		
	ids_H = dict()	

	while (len(layer_G) == 0 or len(layer_H) == 0):
		# process a layer in G
		layer_G_code = set()
		while (visited_G[layer_G[-1]] == 1)	:
			v = layer_G.pop()
	 		children = []
			for i in len(G.graph[v]):
				if visited_G[i] == 0:
					children.append(i)
			if (children not in indexes):
				idx += 1
				indexes[children] = idx
			ids_G[v] = indexes[children]
			layer_G_code.append(idx)
			# push the parent onto the stack
			for i in len(G.graph[v]):
				if visited_G[i] == 0:
					children.append(i)
					visited_G[i] = 1
		
		# process a layer in H
		layer_H_code = set()
		while (visited_H[layer_H[-1]] == 1)	:
			v = layer_H.pop()
	 		children = []
			for i in len(H.graph[v]):
				if visited_H[i] == 0:
					children.append(i)
			if (children not in indexes):
				idx += 1
				indexes[children] = idx
			ids_H[v] = indexes[children]
			layer_H_code.append(idx)
			# push the parent onto the stack
			for i in len(H.graph[v]):
				if visited_H[i] == 0:
					children.append(i)
					visited_H[i] = 1

		if (layer_G_code != layer_H_code):
			return False

	return (ids_G[G.root] == idx_H[H.root])

def __main__():
	line = input().split()
	n = int(line[0])
	m = int(line[1]) 
	G = Tree(n, m)
	for i in range(m):
		line = input().split()
		G.add_edge(int(line[0]), int(line[1]))

	line = input().split()
	n = int(line[0])
	m = int(line[1]) 
	H = Tree(n, m)
	for i in range(m):
		line = input().split()
		H.add_edge(int(line[0]), int(line[1]))
	
	if (isomorphic(G, H) == True):
		print("YES", end='')
	else:
		print("NO", end='')

__main__()
