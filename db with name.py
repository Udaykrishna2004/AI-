% Define facts for the database
dob(john, date(1990, 5, 15)).
dob(susan, date(1985, 10, 3)).
dob(michael, date(1995, 2, 20)).
dob(linda, date(1978, 8, 12)).

% Query to find someone's date of birth
get_dob(Name, DOB) :-
    dob(Name, DOB).

% Query to find all people born in a given year
born_in_year(Year, Name) :-
    dob(Name, date(Year, _, _)).

% Query to find all people born in a given month
born_in_month(Month, Name) :-
    dob(Name, date(_, Month, _)).

% Query to find all people born on a given day
born_on_day(Month, Day, Name) :-
    dob(Name, date(_, Month, Day)).
