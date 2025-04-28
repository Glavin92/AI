mother(celestine, arun).
mother(celestine, hilda).
mother(mary, gregory).
mother(mary, rita).
mother(hilda, glavin).
mother(hilda, glenn).

father(marcel, arun).
father(marcel, hilda).
father(felix, gregory).
father(felix, rita).
father(gregory, glavin).
father(gregory, glenn).
father(arun, aston).



parent(M, F, C) :- 
    (mother(M, C), father(F, C)).

grandparent(GM, GF, C) :-
    mother(M,C), mother(GM,M);
	father(F,C), mother(GM,F);
	mother(M,C), father(GF,M);
	father(F,C), father(GF,F).


sibling(C, S) :-
    
    (father(F,C),father(F,S)),
     C \= S.

uncle(U, C) :-
    ((sibling(F, U), father(F, C)); 
    (sibling(M, U), mother(M, C))),
    M \= U. 

aunt(A, C) :-
    ((sibling(F, A), father(F, C)); 
    (sibling(M, A), mother(M, C))),
    F \= A.

cousin(A, U, C, CO) :-
    (aunt(A, C), mother(A, CO)); 
    (uncle(U, C), father(U, CO)).