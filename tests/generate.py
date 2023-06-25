import subprocess
import random

name = "generate_dags.py"

# flags
# a - small dag
# t - tree

flag = 't'

if flag == 't':
	curr = 0
	done = 2476
	for isomorphic in [0, 1]:
		n = 4
		while (n < 300000):
			bound = 8
			if (n <= 16):
				bound = (n-1)*(n-2)
			for i in range(bound):
				curr += 1
				if (1):
					status = round(100*curr/done, 2)
					print(str(status)+'%')
					m = random.randint(n, int(n*(n-1)/2))
					infile = open('dag_'+str(n)+'_'+str(i)+'_'+flag+'_'+str(isomorphic)+'.in', 'w')
					subprocess.run(['python', name, str(n), str(m), str(isomorphic)], stdout=infile)
					infile.close()
					outfile = open('dag_'+str(n)+'_'+str(i)+'_'+flag+'_'+str(isomorphic)+'.out', 'w')
					if (isomorphic == 1):
						outfile.write("YES")
					else:
						outfile.write("NO")
					outfile.close()
			if (n <= 16):
				n += 1
			else:
				n *= 2

	#print(curr)
else:
	curr = 0
	done = 2*(6+10+15+21+28+36)
	for isomorphic in [0, 1]:
		for n in range(4, 10):
			for i in range((n*(n-1)//2)):
				curr += 1
				status = round(100*curr/done, 2)
				print(str(status)+'%')
				m = random.randint(n, int(n*(n-1)/2))
				infile = open('dag_'+str(n)+'_'+str(i)+'_'+flag+'_'+str(isomorphic)+'.in', 'w')
				subprocess.run(['python', name, str(n), str(m), str(isomorphic)], stdout=infile)
				infile.close()
				outfile = open('dag_'+str(n)+'_'+str(i)+'_'+flag+'_'+str(isomorphic)+'.out', 'w')
				if (isomorphic == 1):
					outfile.write("YES")
				else:
					outfile.write("NO")
				outfile.close()
