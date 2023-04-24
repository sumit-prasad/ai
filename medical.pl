symptom(Patient,fever) :- 
verify(Patient," have a fever (y/n) ?").
symptom(Patient,headache) :- 
verify(Patient," have a headache (y/n) ?").
symptom(Patient,cough) :- 
verify(Patient," have a cough (y/n) ?").
symptom(Patient,sneezing) :- 
verify(Patient," have a sneezing (y/n) ?").

ask(Patient,Question) :-
    write(Patient),write(', do you'),write(Question),
    read(N),
    ( (N == yes ; N == y)
      ->
       assert(yes(Question)) ;
       assert(no(Question)), fail).
    
:- dynamic yes/1,no/1.        
    
verify(P,S) :-
   (yes(S) -> true ;
    (no(S) -> fail ;
     ask(P,S))).
     
undo :- retract(yes(_)),fail. 
undo :- retract(no(_)),fail.
undo.

hypothesis(Patient,common_cold) :-
symptom(Patient,headache),
symptom(Patient,sneezing).

hypothesis(Patient,covid) :-
symptom(Patient,fever),
symptom(Patient,headache),
symptom(Patient,cough).