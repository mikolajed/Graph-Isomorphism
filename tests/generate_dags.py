import sys
import random
#import time

def random_permutation(arr):
	def rotate(j, arr):
		b = arr[j-1]
		while (j>1):
			arr[j-1]=arr[j-2]
			j -= 1
		arr[0] = b
		return arr

	n = len(arr)
	perm_number = n

	j = n
	i = 2
	while (j>1):
		if (i == perm_number):
			return arr
		rotate(j, arr)
		if (j!=arr[j-1]):
			i += 1
			j = n
		else:
			j -= 1
		
args = sys.argv

if (len(args) < 3):
	 exit(1)

n = int(args[1])
m = int(args[2])
isomorphic_true = int(args[3]);

def has_cycle(graph):
	visited = set()
	stack = set()

	def dfs(node):
		visited.add(node)
		stack.add(node)

		for neighbor in range(len(graph)):
			if (graph[node][neighbor]):
				if neighbor in stack:
					return True
				if neighbor not in visited and dfs(neighbor):
					return True

		stack.remove(node)
		return False

	for node in range(len(graph)):
		if node not in visited and dfs(node):
			return True

	return False

def generate_dag(num_nodes):
	# Create an empty adjacency matrix
	adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]

	# Generate random edges
	edges = []
	candidates = []
	for i in range(n):
		for j in range(n):
			candidates.append((i, j))

	dense = 0
	m = random.randint(n, n*(n-1)//2)
	while (len(candidates) and (dense or len(edges) < m)):
		idx = random.randint(0, len(candidates)-1)
		source = candidates[idx][0]
		target = candidates[idx][1]
		candidates[idx] = candidates[-1]
		candidates.pop()
		if (source != target and (target, source) not in edges):
		   adjacency_matrix[source][target] = 1
		   if (has_cycle(adjacency_matrix)):
			   adjacency_matrix[source][target] = 0
		   else:
			   edges.append((source, target))

	return edges

def generate_two_dags(n):
	edges = generate_dag(n)
	
	# one random bijection which maps nodes between two dags
	perm = random_permutation(list(range(n)))
	f = lambda i: perm[i]

	edges2 = []
	# creating the second dag and printing all the results
	for ele in edges:
		edges2.append(ele)

	# create different dags which are as similars as possible but with two different edges deleted	
	if (isomorphic_true == 0):	
		edges[0] = edges[-1]
		edges.pop()
		edges2[1] = edges2[-1]
		edges2.pop()
	
	print(n, len(edges))
	for e in edges:
		print(e[0], e[1])

	print(n, len(edges2))
	for e in edges2:
		print(f(e[0]), f(e[1]))

def generate_tree(n):
	edges = []
	vertices = set()

	#root = 0
	root = random.randint(0, n-1)
	vertices.add(root)

	for i in range(n):
		if i != root:
			parent = random.choice(list(vertices))
			vertices.add(i)
			edges.append((parent, i))

	return edges

def generate_two_trees(n):
	edges = generate_tree(n)
	
	# one random bijection which maps nodes between two dags
	#perm = random_permutation(list(range(n)))
	perm = list(range(n))

	if (isomorphic_true == 1):	
		for i in range(len(perm)):
			perm[i] = (perm[i] + 11)%n
	f = lambda i: perm[i]

	edges2 = []
	# creating the second dag and printing all the results
	for ele in edges:
		edges2.append(ele)

	# create different dags which are as similars as possible but with two different edges deleted	
	if (isomorphic_true == 0):	
		edges2[1] = ( (list(edges2[1])[0] + 1)%2, edges2[1][1])
		# COMMENTED PART IS FOR UNTDIRECTED TREES, and has a bug
		# find a leaf and change its parent
		#degree = [0] * n
		#for v, u in edges2:
		#	# add to a parent
		#	degree[v] += 1
		#leaves = []
		#for i in range(n):
		#	if degree[i] == 0:
		#		leaves.append(i)
		#for i in range(len(edges2)):
		#	v, u = edges2[i]
		#	if u == leaves[0]:
		#		if len(leaves) > 1:
		#			edges2[i] = (leaves[1], edges2[i][1])
		#		#the tree is a just a single path
		#		else:
		#			edges2[i] = ((i+1)%n, edges2[i][1])
		#		break
	
	print(n, len(edges))
	for e in edges:
		print(e[0], e[1])

	print(n, len(edges2))
	for e in edges2:
		print(f(e[0]), f(e[1]))

generate_two_trees(n)
#generate_two_dags(n)
