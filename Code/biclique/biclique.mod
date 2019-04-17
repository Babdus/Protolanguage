param n;
param m;
set rows := 1..n;
set cols := 1..m;
param M {rows,cols};

var X {i in rows} binary;
var Y {j in cols} binary;
var Z {i in rows, j in cols} binary;

maximize Number_Of_Edges:
	(sum {i in rows, j in cols} Z[i,j]);

subject to Only_Existing_Egdes_Included {i in rows, j in cols}:
	X[i] + Y[j] <= M[i,j] + 1;

subject to Choose_Rows_Accordingly {i in rows, j in cols}:
	Z[i,j] <= X[i];

subject to Choose_Cols_Accordingly {i in rows, j in cols}:
	Z[i,j] <= Y[j];
