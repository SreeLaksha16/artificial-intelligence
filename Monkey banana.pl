% State representation: state(MonkeyPos, BoxPos, MonkeyOnBox?, HasBanana?)
move(state(middle, middle, onbox, no), grab, state(middle, middle, onbox, yes)).
move(state(X, X, floor, H), climb, state(X, X, onbox, H)).
move(state(X, Y, floor, H), push(X, Y), state(Y, Y, floor, H)).
move(state(X, Y, floor, H), walk(X, Y), state(Y, Y, floor, H)).

canget(state(_, _, _, yes)).
canget(State1) :-
    move(State1, _, State2),
    canget(State2).
