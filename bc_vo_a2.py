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

from codecs import utf_8_encode
import json
# global variable 
json_file = "movies_list.json"
MovieList = []

def read_json_file(filename): 
    # reading file
    # opening the file with special encoding to ready 
    # side note to self why is the encoding needed?
    File = open(filename, 'r', encoding="utf-8") 
    # loading the json file
    FileData = json.load(File)  
    # side note to self 
    # FileData is a list of dictionaries
    # closing the file
    File.close()

    # json to object
    for i in FileData:
        MovieList.append(Movie(i["title"], i["year"], i["cast"], i["genres"]))
    
class Movie:
    def __init__(self, title, year, cast, genres):
        self.title = title
        self.year = year
        self.cast = cast
        self.genres = genres  
                                                                              

def print_menu():
    print("[I] Movie information overview")
    print("[M] Make modification based on assignment")
    print("[S] Search a movie title")
    print("[C] Change title and/or release year by search on title")
    print("[Q] Quit program")


def countobjectforfilter(objectlist):
    # count the object
    count = 0
    for obj in objectlist:
        count += 1
    return count

def printobjectforfilter(objectlist):
    # print the object
    # return the object
    string = ""
    for obj in objectlist:
        tempstring = "title = {0}, year = {1}, cast = {2}, genres = {3}\n"
        string += tempstring.format(obj.title, obj.year, obj.cast, obj.genres)
    return string

def print_movie_info():
    # this function is maybe hardcoded
    #TODO- The number of movies released in 2004.
    print("The number of movies released in 2004:\n" + str(countobjectforfilter(filter(lambda Listmovies : Listmovies.year == 2004, MovieList))))
    #TODO- The number of movies in which the genre is Science Fiction.
    print("The number of movies in which the genre is Science Fiction: \n" + str(countobjectforfilter(filter(lambda Listmovies : "Science Fiction" in Listmovies.genres, MovieList))))
    #TODO- All movies with actor Keanu Reeves.
    print("All movies with actor Keanu Reeves: \n" + printobjectforfilter(filter(lambda Listmovies : "Keanu Reeves" in Listmovies.cast , MovieList)))
    #TODO- All movies with actor Sylvester Stallone released between 1995 and 2005.
    print("All movies with actor Sylvester Stallone released between 1995 and 2005: \n" + printobjectforfilter(filter(lambda Listmovies : "Sylvester Stallone" in Listmovies.cast and Listmovies.year >= 1995 and Listmovies.year <= 2005, MovieList)))

def make_modification_based_on_assignment():
    print("Make modification based on assignment")
    #TODO- Change the release year from the movie Gladiator from 2000 to 2001.
    
    #TODO- Set the release year from the oldest movie to one year earlier.
    #TODO- Actor Natalie Portman changed her name to Nat Portman. Adjust this at all movies she is in.
    #TODO- Actor Kevin Spacey got cancelled. Remove his name from all movies he is in.


def main():
    # TODO: implement the body of the function. For each option implement a separate function.
    read_json_file(json_file)
    pass


if __name__ == "__main__":
    main()
    print_movie_info()
    with open ("movies_list.json", "r", encoding="utf-8") as outfile:
        d = json.load(outfile)
    with open ("special_movies_list.json", "w",encoding="utf-8",) as outfile:
        json.dump(d, outfile, indent=4)