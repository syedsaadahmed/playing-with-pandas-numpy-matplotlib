import numpy as np

with open('graph.dat') as f:
    content = f.readlines()
    content = content[2:]

content = [elem.strip() for elem in content]

#Identity matrix of order 8x8
Id_M = np.identity(8,dtype = int)

#for empty matrix of order 8x8
row,col = 8,8
col = 8
Mat = [ [ 0 for i in range(row) ] for j in range(col) ]

#for evaluating adjacency matrix using nodes given in graph.dat file
for val in content:
	x=int(val.split(' ')[0])-1
	y=int(val.split(' ')[1])-1
	Mat[x][y] = 1
	Mat[y][x] = 1

mod_Mat = np.add(Mat,Id_M)

v_val = 0
answer = {}

for vec in Id_M:
    res = []
    res = np.matmul(vec, mod_Mat)
    res = np.matmul(res, mod_Mat)
    for values in range(len(res)):
    	if res[values] > 0:
    		res[values] = 1
    v_val = v_val+1

    print("Result " + str(res) + " for Node = " + str(v_val))
    answer.update({"Node_"+str(v_val):res.sum()})

print("So " + max(answer, key=answer.get) + ", will be the starting node for the meme.")

