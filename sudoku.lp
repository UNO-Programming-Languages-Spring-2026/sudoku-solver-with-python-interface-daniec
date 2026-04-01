% Sudoku Solver
%
% Hints:
% For subgrid of size n, subgrids can be identified by labels 1..n*n
% A cell (x,y) can be mapped to the subgrid labeled 1+(((x-1)/n)*n+(y-1)/n)

% Your implementation please...
#const n = 9.

row(1..n).
col(1..n).
num(1..n).
% achieved: rows, columns, and numbers range from 1 to n.

subgrid_size(S) :- S = 1..n, S*S = n.
% achieved: S is the size of each subgrid, derived from n using S*S = n.

subrow(X,SR) :- row(X), subgrid_size(S), SR = (X-1)/S.
% achieved: SR is the subgrid-row index of X.

subcol(Y,SC) :- col(Y), subgrid_size(S), SC = (Y-1)/S.
% achieved: SC is the subgrid-column index of Y.

subgrid(X,Y,G) :-
    subrow(X,SR), subcol(Y,SC), subgrid_size(S),
    G = 1 + SR*S + SC.
% achieved: each cell (X,Y) is mapped to subgrid G.

1 { sudoku(X,Y,N) : num(N) } 1 :- row(X), col(Y).
% achieved: each cell (X,Y) contains exactly one number N from {1..n}.

sudoku(X,Y,N) :- initial(X,Y,N).
:- initial(X,Y,N1), sudoku(X,Y,N2), N1 != N2.
% achieved: if a cell has an initial value, the solution must use that value and no other.

:- sudoku(X,Y1,N), sudoku(X,Y2,N), Y1 != Y2.
% achieved: no row contains the same number twice.

:- sudoku(X1,Y,N), sudoku(X2,Y,N), X1 != X2.
% achieved: no column contains the same number twice.

:- subgrid(X1,Y1,G), subgrid(X2,Y2,G), sudoku(X1,Y1,N), sudoku(X2,Y2,N), X1 != X2; Y1 != Y2.
% achieved: no subgrid contains the same number twice.

#show sudoku/3.