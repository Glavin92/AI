mother(sangama, mathew).
mother(sangama, chitra).
mother(philomena, rita).
mother(philomena, glady).
mother(rita, manoah).
mother(rita, gideon).
mother(glady, carol).
mother(chitra, deepak).
mother(chitra, asha).

father(manick, mathew).
father(manick, chitra).
father(fedrich, rita).
father(fedrich, glady).
father(mathew, manoah).
father(mathew, gideon).
father(shivraj, deepak).
father(shivraj, asha).
father(ronald, carol).

parent(P, C) :-
    mother(P, C);
    father(P, C).

siblings(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

brother(B, S) :-
    siblings(B, S),
    male(B).

sister(S, B) :-
    siblings(S, B),
    female(S).

uncle(Uncle, Child) :-
    parent(P, Child),
    siblings(Uncle, P),
    male(Uncle).

aunt(Aunt, Child) :-
    parent(P, Child),
    siblings(Aunt, P),
    female(Aunt).

grandfather(GF, Child) :-
    father(GF, P), 
    parent(P, Child).

grandmother(GM, Child) :-
    mother(GM, P),
    parent(P, Child).

cousin(Cousin, Child) :-
    parent(P1, Child),
    parent(P2, Cousin),
    siblings(P1, P2),
    Child \= Cousin.


male(mathew).
male(deepak).
male(manoah).
male(gideon).
male(manick).
male(fedrich).
male(shivraj).
male(ronald).

female(chitra).
female(asha).
female(rita).
female(glady).
female(carol).
female(sangama).
female(philomena).


/*
1. Save this file with the extension `.pl`, e.g., family.pl

2. Open SWI-Prolog (or any Prolog interpreter).

3. Load the file by typing:
   ?- [family].

4. Now you can make queries, for example:

   % Find Manoah's parents
   ?- parent(X, manoah).

   % Find Manoah's siblings
   ?- siblings(manoah, Sibling).

   % Find who is Manoah's uncle
   ?- uncle(Uncle, manoah).

   % Find Manoah's grandparents
   ?- grandfather(GF, manoah).
   ?- grandmother(GM, manoah).

   % Find who are Manoah's cousins
   ?- cousin(Cousin, manoah).

5. To exit, type:
   ?- halt.
*/