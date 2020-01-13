# import random
# import matplotlib.pyplot as plt
# import numpy as np

# #graph dict with node and degree 
# graph = {1:[2]}

# #100 instead of 10000
# for i in range(2, 1000):
# 	node_next = random.randint(1,i)
# 	while ( node_next == i):
# 		node_next = random.randint(1,i)
# 	graph[i] = [node_next]


# degrees = []
# for node in graph:
#     degreeinout = 0
#     if node in graph:
#     	degreeinout = len(graph[node])
#     	for x in graph:
#     		if node in graph[x]:
#     			degreeinout = degreeinout + 1
#     degrees.append(degreeinout)

# plt.plot(degrees)
# plt.title('Graph for Distribution')
# plt.ylabel('In-Out degree of each node')
# plt.xlabel('number of nodes')
# plt.show()



# from math import log, e

# def calcEntropy(array_of_degrees):
# 	array_of_degrees = np.array(array_of_degrees)
# 	total_count = len(array_of_degrees)
# 	if total_count <= 1:
# 		return 0
# 	value,counts = np.unique(array_of_degrees, return_counts=True)
# 	norm_counts = counts / total_count
# 	base=2
# 	return -(norm_counts * np.log(norm_counts)/np.log(base)).sum()

# print("calculated Entropy will for be Distribution will be " + str(calcEntropy(degrees)))













import random
import matplotlib.pyplot as plt
import numpy as np

#graph dict with node and degree 
graph = {1:[2]}

#100 instead of 10000
for i in range(2, 1000):
	next_node = random.randint(1,i)
	graph[i] = [next_node]

degree = []
for vertex in graph:
    degreeinout = 0
    if vertex in graph:
    	degreeinout = len(graph[vertex])
    	for x in graph:
    		if vertex in graph[x]:
    			degreeinout = degreeinout + 1
    degree.append(degreeinout)

plt.plot(degree)
plt.title('Graph for Degree Distribution')
plt.ylabel('In-Out Degree of each node')
plt.xlabel('Number of nodes')
plt.show()




from math import log, e

def calcEntropy(array_of_degrees):
	array_of_degrees = np.array(array_of_degrees)
	total_count = len(array_of_degrees)
	if total_count <= 1:
		return 0
	value,counts = np.unique(array_of_degrees, return_counts=True)
	norm_counts = counts / total_count
	base=2
	return -(norm_counts * np.log(norm_counts)/np.log(base)).sum()

print("calculated Entropy will for be Distribution will be " + str(calcEntropy(degree)))



