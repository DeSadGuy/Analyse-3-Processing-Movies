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
test_json_file = "test_movies_list.json"

def print_menu():
    print("[I] Movie information overview")
    print("[M] Make modification based on assignment")
    print("[S] Search a movie title")
    print("[C] Change title and/or release year by search on title")
    print("[Q] Quit program")

def print_movie_info():
    # this function is maybe hardcoded but it works
    print("The number of movies released in 2004: \n" + str(SpecialFunctions.count_filtered_object(filter(lambda Listmovies : Listmovies["year"] == 2004, SpecialFunctions.Read_Json_file()))))
    print("---------------------")
    print("The number of movies in which the genre is Science Fiction: \n" + str(SpecialFunctions.count_filtered_object(filter(lambda Listmovies : "Science Fiction" in Listmovies["genres"], SpecialFunctions.Read_Json_file()))))
    print("---------------------")
    print("All movies with actor Keanu Reeves: \n" + SpecialFunctions.print_filtered_objects(filter(lambda Listmovies : "Keanu Reeves" in Listmovies["cast"] , SpecialFunctions.Read_Json_file())))
    print("---------------------")
    print("All movies with actor Sylvester Stallone released between 1995 and 2005: \n" + SpecialFunctions.print_filtered_objects(filter(lambda Listmovies : "Sylvester Stallone" in Listmovies["cast"] and Listmovies["year"] >= 1995 and Listmovies["year"] <= 2005, SpecialFunctions.Read_Json_file())))

def make_modification_based_on_assignment():
    print("Make modification based on assignment")
    #NOTES using temp variable for testing purposes

    #TODO- Change the release year from the movie Gladiator from 2000 to 2001.
    print("change the release year from the movie Gladiator from 2000 to 2001.")
    data = SpecialFunctions.Read_Json_file()
    for movie in data:
        if movie["title"].casefold() == "Gladiator".casefold() and movie["year"] == 2000:
            movie["year"] = 2001
    SpecialFunctions.Write_Json_file(data)
    

    #TODO- Set the release year from the oldest movie to one year earlier.
    data = SpecialFunctions.Read_Json_file()
    oldest_movie = data[0]
    for movie in data:
        if movie["year"] < oldest_movie["year"]:
            oldest_movie = movie
    print("old ---------------------------")
    print(oldest_movie)
    for movie in data:
        if movie["title"].casefold() == oldest_movie["title"].casefold():
            movie["year"] -= 1
            print("new ---------------------------")
            print(movie)
    SpecialFunctions.Write_Json_file(data)
    print("---------------------------")
    #TODO- Actor Natalie Portman changed her name to Nat Portman. Adjust this at all movies she is in.
    print("actor Natalie Portman changed her name to Nat Portman. Adjust this at all movies she is in.")
    data = SpecialFunctions.Read_Json_file()
    for movie in data:
        if "Natalie Portman" in movie["cast"]:
            print("before ---------------------------")
            print(movie)
            movie["cast"].remove("Natalie Portman")
            movie["cast"].append("Nat Portman")
            print("after ---------------------------")
            print(movie)
    
    SpecialFunctions.Write_Json_file(data)
    print("---------------------------")


    #TODO- Actor Kevin Spacey got cancelled. Remove his name from all movies he is in.
    print("Actor Kevin Spacey got cancelled. Remove his name from all movies he is in.")

    data = SpecialFunctions.Read_Json_file()
    for movie in data:
        if "Kevin Spacey" in movie["cast"]:
            print("before ---------------------------")
            print(movie)
            movie["cast"].remove("Kevin Spacey")
            print("after ---------------------------")
            print(movie)
    
    SpecialFunctions.Write_Json_file(data)
    print("---------------------------")

def search_movie_title():
    pass 
    print("search movie title")
    userinput = input("Enter your input: ")
    result = SpecialFunctions.search_object_by_title_singleoutput(userinput)
    if result == None:
        print("No movie found")
    else:
        print(result)
    print("---------------------------")



def main():
    # TODO: implement the body of the function. For each option implement a separate function.
    print_menu()
    takinginput()
    

def takinginput():
    userinput = input("Enter your input: ")
    userinput = userinput.upper()
    userinput = userinput.strip()
    if userinput == "I":
        print_movie_info()
    elif userinput == "M":
        make_modification_based_on_assignment()
    elif userinput == "S":
        search_movie_title()
        pass
    elif userinput == "C":
        pass
    elif userinput == "Q":
        exit()
    else:
        print("Invalid input")
        takinginput()


class SpecialFunctions: 
    @staticmethod
    def Read_Json_file():
        with open(json_file, "r", encoding="utf-8") as data_file:
            data = json.load(data_file)
            return data

    @staticmethod
    def Write_Json_file(data):
        with open(test_json_file, "w", encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=4)

    @staticmethod
    def Change_release_year(new_year, title):
        data = SpecialFunctions.Read_Json_file()
        for movie in data:
            if movie["title"].casefold() == title.casefold():
                movie["year"] = new_year
        SpecialFunctions.Write_Json_file(data)

    @staticmethod   
    def Change_Title(new_title, title):
        data = SpecialFunctions.Read_Json_file()
        for movie in data:
            if movie["title"].casefold() == title.casefold():
                movie["title"] = new_title
        SpecialFunctions.Write_Json_file(data)

    @staticmethod
    def filter_object():
        pass
        return filtered_object

    @staticmethod
    def search_object_by_title(title):
        data = SpecialFunctions.Read_Json_file()
        filtered_objects = filter(lambda data : title.casefold() in data["title"].casefold(), data)
        filtered_objects = SpecialFunctions.print_filtered_objects(filtered_objects)
        return filtered_objects
    
    @staticmethod
    def search_object_by_title_singleoutput(title):
        data = SpecialFunctions.Read_Json_file()
        for movie in data:
            if title.casefold() == movie["title"].casefold():
                return movie
        return None

    @staticmethod
    def print_filtered_objects(filtered_objects):
        string = ""
        for obj in filtered_objects:
            tempstring = "title = {0}, year = {1}, cast = {2}, genres = {3}\n"
            string += tempstring.format(obj["title"], obj["year"], obj["cast"], obj["genres"])
        return string
    
    @staticmethod
    def count_filtered_object(filtered_objects):
        # count the object
        count = 0
        for obj in filtered_objects:
            count += 1
        return count

if __name__ == "__main__":
    main()
    


