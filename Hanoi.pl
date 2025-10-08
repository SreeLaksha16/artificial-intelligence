move(1, A, _, C) :- format('Move disk from ~w to ~w~n', [A, C]).
move(N, A, B, C) :-
    N > 1, M is N-1,
    move(M, A, C, B),
    move(1, A, B, C),
    move(M, B, A, C).