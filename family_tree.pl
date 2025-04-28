% --------- Family Facts ---------

% Mothers
mother(sangama, mathew).
mother(sangama, chitra).
mother(philomena, rita).
mother(philomena, glady).
mother(rita, manoah).
mother(rita, gideon).
mother(glady, carol).
mother(chitra, deepak).
mother(chitra, asha).

% Fathers
father(manick, mathew).
father(manick, chitra).
father(fedrich, rita).
father(fedrich, glady).
father(mathew, manoah).
father(mathew, gideon).
father(shivraj, deepak).
father(shivraj, asha).
father(ronald, carol).

% --------- Rules ---------

% P is a parent of C if P is mother or father of C
parent(P, C) :-
    mother(P, C);
    father(P, C).

% X and Y are siblings if they share a parent and are not the same person
siblings(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

% B is a brother of S if B and S are siblings and B is male
brother(B, S) :-
    siblings(B, S),
    male(B).

% S is a sister of B if S and B are siblings and S is female
sister(S, B) :-
    siblings(S, B),
    female(S).

% Uncle is a male sibling of one of the child's parents
uncle(Uncle, Child) :-
    parent(P, Child),
    siblings(Uncle, P),
    male(Uncle).

% Aunt is a female sibling of one of the child's parents
aunt(Aunt, Child) :-
    parent(P, Child),
    siblings(Aunt, P),
    female(Aunt).

% Grandfather is the father of a parent of the child
grandfather(GF, Child) :-
    father(GF, P), 
    parent(P, Child).

% Grandmother is the mother of a parent of the child
grandmother(GM, Child) :-
    mother(GM, P),
    parent(P, Child).

% Cousin relationship
cousin(Cousin, Child) :-
    parent(P1, Child),
    parent(P2, Cousin),
    siblings(P1, P2),
    Child \= Cousin.

% --------- Important Note ---------
% You must also define who is male and who is female
% Add gender facts to avoid errors for brother/sister/uncle/aunt queries.

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

% --------- How to run this Prolog program ---------

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