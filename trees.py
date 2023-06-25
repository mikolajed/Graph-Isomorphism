import queue

class Tree:
	def __init__(self, n, m, root=0, edges=[]):
		self.root = root
		self.num_nodes = n
		self.num_edges = m
		self.children = []
		self.parent = [-1] * n
		self.depth = []
		self.height = []	# maximal path down the tree from a node
		# if not a tree
		if (m != n-1):
			exit(0)

		self.children = [[] for _ in range(self.num_nodes)]
		# edges are in form (parent of v, v)
		for edge in edges:
			u, v = edge
			self.children[u].append(v)
			# self.children[v].append(u)
			if self.parent[v] != -1:
				print("NOT A TREE")
				exit(1)
			self.parent[v] = u

	def add_edge(self, u, v):
		self.children[u].append(v)
		# self.children[v].append(u)
		if self.parent[v] != -1:
			print("NOT A TREE")
			exit(1)
		self.parent[v] = u

	def calculate_depths(self, v=0, d=0, parent=-1):
		self.depth = [0] * self.num_nodes
		self.recalculate_depths(v, d, parent)
	
	def recalculate_depths(self, v=0, d=0, parent=-1):
		self.depth[v] = d	
		for u in self.children[v]:
			if u != parent:
				self.recalculate_depths(u, d+1, v)

	def calculate_heights(self, v=0, parent=-1):
		self.height = [0] * self.num_nodes
		self.recalculate_heights(v, parent)
	
	def recalculate_heights(self, v=0, parent=-1):
		height = 1
		for u in self.children[v]:
			if u != parent:
				self.recalculate_heights(u, v)
				if height < self.height[u] + 1:
					height = self.height[u] + 1
		self.height[v] = height
		
	# finds the longest path in the tree with undirected edges 
	# we take the root as the middle node on the longest path
	# there can be at most two roots - one for odd-length path, two for even-lenth path
	# THE FUNCTION ALWAYS RETURNS TWO ROOTS, the second returned might not be a root
	# ALGORITHM:
	# observation 1: the set of leaves contains both ends of the longest path
	# in each interation the algorithm removes all leaves from the tree ("cuts them")
	# a new obtained tree has the same the same property (observation 1) as the previous tree
	# in the last iteration we will be left with on or two nodes - the roots
	def find_roots(self):
		q = queue.Queue()

		# visited child count
		vcc = [0] * self.num_nodes		
		# find leaves
		for i in range(self.num_nodes):	
			if len(self.children[i]) == 1:
				q.put(i)

		order = []
		while not q.empty():
			v = q.get()
			order.append(v)
			for u in self.children[v]:
				# we found a parent of v, a leaf in the next tree
				if vcc[u] + 1 == len(self.children[u]) - 1:
					vcc[u] += 1
					q.put(u)
				# we found a parent of v, not a patent in the next tree 
				elif vcc[u] != len(self.children[u]):
					vcc[u] += 1

		# in case of only one root it will not go into the queue
		if len(order) != self.num_nodes:
			for i in range(self.num_nodes):
				if vcc[i] == len(self.children[i]):
					order.append(i)

		# the roots are last nodes to be processed
		if len(order) == 1:
			return order[-1], order[-1]
		else:
			# the first value is a root, the second is not if the is only one root in the tree
			return order[-1], order[-2]
		
	def print_graph(self):
		for i, adj_list in enumerate(self.children):
			print(f"Node {i}: {adj_list}")


def check_isomorphism_rooted(G, root_G, H, root_H):
	G.calculate_depths(root_G)
	H.calculate_depths(root_H)
	# order to process nodes based on their depths
	order_G = dict()
	order_H = dict()
	for i in range(G.num_nodes):
		if (G.depth[i] not in order_G):
			order_G[G.depth[i]] = []
		order_G[G.depth[i]].append(i)
	for i in range(H.num_nodes):
		if (H.depth[i] not in order_H):
			order_H[H.depth[i]] = []
		order_H[H.depth[i]].append(i)
	order_G = dict(sorted(order_G.items(), key=lambda x: x[0], reverse=True))
	order_H = dict(sorted(order_H.items(), key=lambda x: x[0], reverse=True))

	# tree dephs of G and H are different
	if len(order_G) != len(order_H):
		return False
		
	# index is associated with a unique number, two nodes have the same index if the multisets of indexes of their children are the same
	indexes_G = [0] * G.num_nodes
	indexes_H = [0] * H.num_nodes
	# all indexes used, shared between two trees
	indexes_used = []
	
	# process each depth starting from leaves of the larges depth
	for i in range(len(order_G)):
		depth_g, nodes_g = list(order_G.items())[i]
		depth_h, nodes_h = list(order_H.items())[i]
		# for each node j in the k-th depth
		layer_G = []
		layer_H = []
		for v in nodes_g:
			children = []
			for u in G.children[v]:
				if G.depth[u] > G.depth[v]:
					children.append(indexes_G[u])
			# check if given multiset of indexes is associated with an index
			children = sorted(children)
			if children in indexes_used:
				idx = indexes_used.index(children)
				indexes_G[v] = idx
			else:
				indexes_used.append(children)
				indexes_G[v] = len(indexes_used) - 1
			layer_G.append(indexes_G[v])
		for v in nodes_h:
			children = []
			for u in H.children[v]:
				if H.depth[u] > H.depth[v]:
					children.append(indexes_H[u])
			# check if given multiset of indexes is associated with an index
			children = sorted(children)
			if children in indexes_used:
				idx = indexes_used.index(children)
				indexes_H[v] = idx
			else:
				indexes_used.append(children)
				indexes_H[v] = len(indexes_used) - 1
			layer_H.append(indexes_H[v])
	
		layer_G = sorted(layer_G)	
		layer_H = sorted(layer_H)
		
		if layer_G != layer_H:
			return False
			
	if indexes_G[root_G] == indexes_H[root_H]:
		return True
	else:
		return False

def is_isomorphic(G, H):
	if (G.num_nodes != H.num_nodes or G.num_edges != H.num_edges):
		return False
	
	# find roots for undirected edges
	# root1g, root2g = G.find_roots()
	# root1h, root2h = H.find_roots() 

	root_g = -1
	for i in range(G.num_nodes):
		if G.parent[i] == -1:
			if root_g == -1:
				root_g = i
			else:
				# not a tree
				print("NOT A TREE")
				exit(1)

	root_h = -1
	for i in range(H.num_nodes):
		if H.parent[i] == -1:
			if root_h == -1:
				root_h = i
			else:
				# not a tree
				print("NOT A TREE")
				exit(1)

	# checks isomorphism of two rooted trees for an undirected tree
	#if check_isomorphism_rooted(G, root1g, H, root1h) or check_isomorphism_rooted(G, root1g, H, root2h):
	#	return True
	#else:
	#	return False

	if check_isomorphism_rooted(G, root_g, H, root_h):
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
