# Analyse-3-Processing-Movies




'''
Problem Statement:
Create a program that can handle movie information from the `movies.json` file. 
Important: 
- Input file will be in the same path as the program file.
- The solution must use Python exception handling constructs to handle possibly raising exceptions.

Step 1. Implement a program that using the data from `movies.json`, shows the following information:
- The number of movies released in 2004.
- The number of movies in which the genre is Science Fiction.
- All movies with actor Keanu Reeves.
- All movies with actor Sylvester Stallone released between 1995 and 2005.


Step 2. Using data from `movies.json`, makes the following adjustments and write it back to the file:
- Change the release year from the movie Gladiator from 2000 to 2001.
- Set the release year from the oldest movie to one year earlier.
- Actor Natalie Portman changed her name to Nat Portman. Adjust this at all movies she is in.
- Actor Kevin Spacey got cancelled. Remove his name from all movies he is in.


Step 3. The Default menu of the program will look like the following. The user has to choose one of the options. 
Option [I] will be based on Step 1, Option [M] will be based on Step 2, Examples for options [S] and [C] are provided below:

[I] Movie information overview
[M] Make modification based on assignment
[S] Search a movie title
[C] Change title and/or release year by search on title
[Q] Quit program


Input example (search):
S
Bambi
Q

Output example (search):
`{'title': 'Bambi', 'year': 1942, 'cast': ['Bambi'], 'genres': ['Children','Action']}`


Input example (modify):
C
Bambi
Bambi Remastered
2023
Q

Output example (modify):
`{'title': 'Bambi Remastered', 'year': 2023, 'cast': ['Bambi'], 'genres': ['Children','Action']}`

Learning Material: Weeks 7,9,10,11 of BaseCamp [https://github.com/hogeschool/basecamp]

'''