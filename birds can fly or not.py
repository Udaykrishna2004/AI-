% Facts about birds and their ability to fly
can_fly(pigeon).
can_fly(sparrow).
can_fly(eagle).
cannot_fly(penguin).
cannot_fly(ostrich).

% Rules to determine if a bird can fly or not
bird_can_fly(Bird) :-
    can_fly(Bird).

bird_can_fly(Bird) :-
    \+ cannot_fly(Bird).

% Queries
% To check if a specific bird can fly
% Example query: bird_can_fly(penguin).
