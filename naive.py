from itertools import permutations
import random

class Graph:
	def __init__(self, n, m=0, edges=[]):
		self.num_nodes = n
		self.num_edges = m
		self.graph = [[0] * self.num_nodes for _ in range(self.num_nodes)]
	
		for edge in edges:
			self.add_edge(edge[0], edge[1])

	def add_edge(self, u, v):
		self.graph[u][v] = 1

def isomorphic(G, H):
	if (G.num_nodes != H.num_nodes or G.num_edges != H.num_edges):
		return False

	n = G.num_nodes

	numbers = list(range(0, n))
	perms = permutations(numbers)
	# check every every bijective mapping of nodes
	for perm in perms:
		bij = list(perm)
		f = lambda i: bij[i]
		found = True
		for i in range(n):
			for j in range(n):
				if (G.graph[i][j] != H.graph[f(i)][f(j)]):
					found = False
		if (found == True):
			return True
	return False

def __main__():
	line = input().split()
	n = int(line[0])
	m = int(line[1]) 
	edges = []
	for i in range(m):
		line = input().split()
		edges.append((int(line[0]), int(line[1])))

	G = Graph(n, m, edges)

	line = input().split()
	n = int(line[0])
	m = int(line[1]) 
	edges = []
	for i in range(m):
		line = input().split()
		edges.append((int(line[0]), int(line[1])))

	H = Graph(n, m, edges)
	#H.print_graph()
	
	if (isomorphic(G, H) == True):
		print("YES", end='')
	else:
		print("NO", end='')
__main__()

#edges = input()
#print(edges)
#if isomorphic(Graph G(input()))
