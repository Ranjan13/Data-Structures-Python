import sys
import time
'''
Expansion of each node is done here
'''
def expand(adj_list,q,e,root):
	q.append(root)
		#print q
	if sys._getframe().f_back.f_code.co_name == 'bfs':
		#for i in range(len(adj_list[root-1])):
		for j in range(len(adj_list[root-1])):
			q.append(adj_list[root-1][j])
		for i in range(len(adj_list)):
			#print "i is ", i
			for j in range(len(adj_list[i])):
				#print "j is ",j
				if adj_list[i][j] not in q:
					q.append(adj_list[i][j])
					
			for k in range(len(q)):
				if q[k] not in e:
					e.append(q[k])

	elif sys._getframe().f_back.f_code.co_name == 'dfs':
		while( len(q) > 0 ):
			#print "Q is",q
			if not(len(q) == 0):
				n = q.pop()
			#print"After pop",q
			for i in range(len(adj_list[n-1])):
			#print "i is",i
				if n not in e:
					q.append(adj_list[n-1][i])
			if n not in e:
				e.append(n)
			#print "Hola! ",e
		#print e
	
def bfs(adj_list):
	#print adj_list
	#print len(adj_list)
	q,e = list(),list()
	root = int(raw_input("Please Enter the Root:"))
	expand(adj_list,q,e,root)
	print "The BFS is:"
	print e
		
def dfs(adj_list):
	q,e = list(),list()
	root = int(raw_input("Please Enter the Root:"))
	expand(adj_list,q,e,root)
	print "DFS is"
	print e
		
'''
The following lines are to get the adjacency list
'''
print "Enter the number of nodes"
node = int(raw_input())
adj_list = [[0 for x in (range(node))] for x in (range(node))]
#print adj_list
print "----Enter the adjacency list: ----"
for i in range(len(adj_list)):
		adj_list[i] = map(int,raw_input().split())
print"----BFS Starts----"
start_time_bfs = time.time()
bfs(adj_list)
end_time_bfs = time.time()
total_bfs_time = end_time_bfs - start_time_bfs
print "and it takes: ", total_bfs_time
print "----BFS Ends----\n"
'''
DFS function starts from here
'''
print"----DFS Starts----"
start_time_dfs = time.time()
dfs(adj_list)
end_time_dfs = time.time()
total_dfs_time =  end_time_dfs - start_time_dfs
print "and it takes: ",total_dfs_time
print"----DFS Ends----"

'''
Calculation for which Algorithm is faster
'''
if ((total_bfs_time - total_dfs_time) > 0):
	print "DFS is faster than BFS"
else:
	print"BFS is faster than DFS"
