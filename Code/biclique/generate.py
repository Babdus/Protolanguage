import sys
import time
import pandas as pd

def generate_list(matrix, output):
	n = len(matrix)
	m = len(matrix[0])
	with open(output, 'w') as out:
		out.write('param n := {};\n'.format(n))
		out.write('param m := {};\n'.format(m))

		out.write('param M :=\n')
		for i in range(n):
			for j in range(m):
				out.write('  {}  {}  {}\n'.format(i+1,j+1,matrix[i][j]))
		out.write(';')

def main(argv):
	df = pd.read_csv(argv[0], index_col=0).fillna('')
	print(df.columns.values.tolist())
	matrix = df.values.tolist()
	print(matrix)
	for i, row in enumerate(matrix):
		for j, cell in enumerate(row):
			matrix[i][j] = 0 if cell.strip() == '' else 1
	print(matrix)

	M = [
		 [1,1,1,0,0,1,0],
		 [1,1,1,0,1,0,0],
		 [1,1,1,0,0,0,1],
		 [0,0,0,1,1,1,1],
		 [0,1,0,1,0,1,1],
		 [1,0,0,1,1,1,0],
		 [0,0,1,1,1,0,1],
		]

	generate_list(matrix, argv[1])

if __name__ == "__main__":
    main(sys.argv[1:])
