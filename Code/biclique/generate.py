def generate_list(matrix):
	n = len(matrix)
	m = len(matrix[0])
	print('param n := {};'.format(n))
	print('param m := {};'.format(m))

	print('param M :=')
	for i in range(n):
		for j in range(m):
			print('  {}  {}  {}'.format(i+1,j+1,matrix[i][j]))
	print(';')

M = [
	 [1,1,1,0,0,1,0],
	 [1,1,1,0,1,0,0],
	 [1,1,1,0,0,0,1],
	 [0,0,0,1,1,1,1],
	 [0,1,0,1,0,1,1],
	 [1,0,0,1,1,1,0],
	 [0,0,1,1,1,0,1],
	]

generate_list(M)