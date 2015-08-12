import sys
'''
def expand(node):
	try:
		choice = int(raw_input("Enter 1 for BFS and 2 for DFS"))
		if(choice == 1):
			bfs(node)
		elif(choice == 2):
			dfs(node)
	except ValueError:
		print "Wrong entry"
'''
def expand(adj_list,q,e,root):
	#m = adj_list[0][0]
	q.append(root)
	#e.append(root)
	if sys._getframe().f_back.f_code.co_name == 'bfs':
		for i in range(len(adj_list)):
			for j in range(len(adj_list[i])):
				if adj_list[i][j] not in q:
					q.append(adj_list[i][j])
	
		for i in range(len(q)):
			if q[i] not in e:
				e.append(q[i])

	elif sys._getframe().f_back.f_code.co_name == 'dfs':
	#This one is for DFS
		while(not(q == None)):
			print "Q is",q
			if not(len(q) == 0):
				n = q.pop()
			print"After pop",q
			#for i in range(len(adj_list[n-1])):
			#print "i is",i
				if n not in e:
					q.append(adj_list[n-1][i])
			if n not in e:
				e.append(n)
			print "Hola! ",e

			#q.append(adj_list[n][ range(len(adj_list[n]))])
			#if n not in e:
			#	e.append(adj_list[n])
			#	print "Hola! ",e

			
		#print len(q)
		#for i in range(len(q),0,-1):	
		print e
def bfs(adj_list):
	print adj_list
	print len(adj_list)
	q,e = list(),list()
	root = int(raw_input("Root:"))
	expand(adj_list,q,e,root)
	print "The BFS is:"
	print e
def dfs(adj_list):
	q,e = list(),list()
	root = int(raw_input("Root:"))
	expand(adj_list,q,e,root)
	print "DFS is"
	print e
	
'''
The following lines are to get the adjacency list
'''

print "Enter the number of nodes"
node = int(raw_input())
adj_list = [[0 for x in (range(node))] for x in (range(node))]
print adj_list
for i in range(len(adj_list)):
	#for j in range(len(adj_list)):
	#print i
	adj_list[i] = map(int,raw_input().split())
#print adj_list[]
bfs(adj_list)
dfs(adj_list)
'''

elif sys._getframe().f_back.f_code.co_name == 'dfs':
	#This one is for DFS
		for i in range(len(adj_list)):
			for j in range(len(adj_list[i])):
				if adj_list[i][j] not in q:
					q.append(adj_list[i][j])
			print "Q is",q
			n = q.pop()
			print"After pop",q
			if n not in e:
				e.append(n)
				print "Hola! ",e


'''
