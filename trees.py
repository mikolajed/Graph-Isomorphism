class Tree:
	def __init__(self, n, m, root=0, edges=[]):
		self.root = root
		self.num_nodes = n
		self.num_edges = m
		self.graph = []
		self.depth = [0] * n
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

	# finds and returns depth of each node in the tree
	# self - graph
	# v - current node
	# d - current depth
	# parent - parent node
	def recalculate_depths(self, v=0, d=0, parent=-1):
		self.depth[v] = d	
		for u in self.graph[v]:
			if u != parent:
				self.recalculate_depths(u, d+1, v)
	
	# finds the longest path in the tree, roots are in the middle
	# there are two roots is the longest path is composed of even number of nodes
	# one root otherwise, however, IN THIS CASE THE SECOND ROOT IS JUST A COPY OF THE FIRST
	# THE FUNCTION ALWAYS RETURNS TWO ROOTS
	def find_roots(self):
		self.recalculate_depths()		
		roots = []

		max_len = 1
		for i in range(self.num_nodes):
			for a in self.graph[i]:
				for b in self.graph[i]:
					if (a != b and self.depth[a] + self.depth[b] + 1):
						max_len = self.depth[a] + self.depth[b] + 1

		longest_path = []
		for i in range(self.num_nodes):
			for a in self.graph[i]:
				for b in self.graph[i]:
					if (max_len == self.depth[a] + self.depth[b] + 1):
						longest_path.append(i)

		# find the nodes in the middle of the longest path
		# find leaves first
		queue = []
		visited = [1] * self.num_nodes
		for i in longest_path:
			visited[i] = 0
		for i in longest_path:
			if len(self.graph[i]):
				queue.append(i)

		topological_order = []
		while len(queue):
			v = queue.pop(0)
			visited[v] = 1
			topological_order.append(v)
			for u in self.graph[v]:
				# find parent
				if visited[u] == 0:
					queue.append(u)

		if (len(longest_path)%2 == 0):
			return topological_order[-1], topological_order[-2]
		else:
			return topological_order[-1], topological_order[-1]
					
	def print_graph(self):
		for i, adj_list in enumerate(self.graph):
			print(f"Node {i}: {adj_list}")


def check_isomorphism_rooted(G, root_G, H, root_H):
	G.recalculate_depths(root_G)
	H.recalculate_depths(root_H)

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
	for depth, nodes in order_G.items():
		# for each node j in the k-th depth
		layer_G = []
		layer_H = []
		for v in nodes:
			children = []
			for u in G.graph[v]:
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
		for v in nodes:
			children = []
			for u in H.graph[v]:
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
	root1g, root2g = G.find_roots() # could be at most two, always returns two
	root1h, root2h = H.find_roots() # could be at most two, always returns two

	# checks isomorphism of two rooted trees
	if check_isomorphism_rooted(G, root1g, H, root1h) or check_isomorphism_rooted(G, root1g, H, root2h):
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
