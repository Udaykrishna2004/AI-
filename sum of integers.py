% Base case: The sum of integers from 1 to 1 is 1.
sum_integers(1, 1).

% Recursive case: Calculate the sum of integers from 1 to N as N + sum of integers from 1 to N-1.
sum_integers(N, Sum) :-
    N > 1,
    M is N - 1,
    sum_integers(M, SubSum),
    Sum is N + SubSum.  
