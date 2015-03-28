import fresh_tomatoes_lisa
import movie

# create the movie instances
frozen = movie.Movie("Frozen",
                     "http://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")
arielle = movie.Movie("The Little Mermaid",
                      "http://upload.wikimedia.org/wikipedia/en/7/75/Movie_poster_the_little_mermaid.jpg",
                      "https://www.youtube.com/watch?v=ur1B_f1FXZ4")
love_actually = movie.Movie("Love Actually",
                      "http://upload.wikimedia.org/wikipedia/en/e/eb/Love_Actually_movie.jpg",
                      "https://www.youtube.com/watch?v=KdzH6a-XEGM")
star_wars_4 = movie.Movie("Star Wars - A New Hope",
                      "http://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                          "https://www.youtube.com/watch?v=9gvqpFbRKtQ")
star_wars_5 = movie.Movie("Star Wars - The Empire Strikes Back",
                      "http://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                          "https://www.youtube.com/watch?v=JNwNXF9Y6kY")
star_wars_6 = movie.Movie("Star Wars - The Return of the Jedi",
                      "http://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg",
                          "https://www.youtube.com/watch?v=CsDwpF3uiZI")

# group the movie instances in a list
my_movies = [frozen, arielle, love_actually, star_wars_4, star_wars_5, star_wars_6]

# use fresh_tomatoes.py to generate the page dynamically from the Python data structure
fresh_tomatoes_lisa.open_movies_page(my_movies)

    
