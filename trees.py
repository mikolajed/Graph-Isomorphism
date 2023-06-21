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
			self.graph[v].append(u)
	
	def add_edge(self, u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)
	
	def print_graph(self):
		for i, adj_list in enumerate(self.graph):
			print(f"Node {i}: {adj_list}")

def is_isomorphic(G, H):
	if (G.num_nodes != H.num_nodes or G.num_edges != H.num_edges):
		return False
	# TODO: find roots
	if check_isomorphism_rooted(G, 0, H, 0):
		return True
	else:
		return False

def check_isomorphism_rooted(G, root_G, H, root_H):
	visited_G= [0] * G.num_nodes
	visited_H= [0] * H.num_nodes
	layer_G = []
	layer_H = []
	# find leaves
	for i in range(G.num_nodes):
		if (len(G.graph[i]) == 1):
			layer_G.append(i)
	for i in range(H.num_nodes):
		if (len(H.graph[i]) == 1):
			layer_H.append(i)

	indexes_G = [0] * G.num_nodes
	indexes_H = [0] * H.num_nodes

	indexes_used = []
	# as long as there is a node to be processed in both graphs
	while (len(layer_G) != 0 and len(layer_H) != 0):
		layer_code_G = []
		layer_code_H = []
		next_layer_G = []
		next_layer_H = []

		# process a layer of outermost non-visited nodes in G
		while (len(layer_G)):
			v = layer_G.pop()
			if visited_G[v] == 1:
				continue
			visited_G[v] = 1
			children = []
			for i in range(len(G.graph[v])):
				if visited_G[i] == 1:
					children.append(indexes_G[i])
			# check if given multiset of indexes is associated with an index
			children = sorted(children)
			if children in indexes_used:
				idx = indexes_used.index(children)
				indexes_G[v] = idx
			else:
				indexes_used.append(children)
				indexes_G[v] = len(indexes_used)
			# find the parent of v, it should be processed in the next layer 
			for i in range(len(G.graph[v])):
				if visited_G[i] == 0 and i != root_G:
					next_layer_G.append(i)
			layer_code_G.append(indexes_G[v])
		
		# process a layer of outermost non-visited nodes in H
		while (len(layer_H)):
			v = layer_H.pop()
			if visited_H[v] == 1:
				continue
			visited_H[v] = 1
			children = []
			for i in range(len(H.graph[v])):
				if visited_H[i] == 1:
					children.append(indexes_H[i])
			# check if given multiset of indexes is associated with an index
			children = sorted(children)
			if children in indexes_used:
				idx = indexes_used.index(children)
				indexes_H[v] = idx
			else:
				indexes_used.append(children)
				indexes_H[v] = len(indexes_used)
			# find the parent of v, it should be processed in the next layer 
			for i in range(len(H.graph[v])):
				if visited_H[i] == 0 and i != root_H:
					next_layer_H.append(i)
			layer_code_H.append(indexes_H[v])
	
		layer_G = [ ele for ele in next_layer_G ]
		layer_H = [ ele for ele in next_layer_H ]
		layer_code_G = sorted(layer_code_G)	
		layer_code_H = sorted(layer_code_H)
		
		if layer_code_G != layer_code_H:
			print("LCG:",layer_code_G)
			print("LCH:",layer_code_H)
			print("I:",indexes_used)
			return False
			
	if indexes_G[root_G] == indexes_H[root_H]:
		return True
	else:
		return False

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
	
	if (is_isomorphic(G, H) == True):
		print("YES", end='')
	else:
		print("NO", end='')

__main__()
