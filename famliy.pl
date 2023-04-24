#PROLOG FAMILY TREE

female(nani). 
female(mom). 
female(sis). 

male(nana).
male(dad).
male(bro).
 
parent(nana,mom).
parent(nani,mom).
parent(dad,bro).
parent(mom,bro).
parent(dad,sis).
parent(mom,sis).


mother(X,Y):- parent(X,Y),female(X). 
father(X,Y):- parent(X, Y),male(X). 
haschild(X):- parent(X,_).
sister(X,Y):- parent(Z,X),parent(Z,Y),female(X),X\==Y. 
brother(X,Y):-parent(Z,X),parent(Z,Y),male(X),X\==Y.