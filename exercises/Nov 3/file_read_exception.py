def get_movies():
    movies = []

    try:
    # read in the movie file and add each movie to the list 
        with open("exercises/Nov 1/movies.txt") as file:
            for line in file: 
                if line.strip() != "":
                 movies.append(line.strip())
    except FileNotFoundError:
        print("Invalid file name")

    return movies 



movies = get_movies()

for movie in movies:
    print(movie)