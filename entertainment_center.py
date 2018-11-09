# import all the required files
import media
import webbrowser
import fresh_tomatoes

# define the movie object
toy_story = media.Movie("Toy Story", "A story of a boy and his toys taht come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc", 1995)


avatar = media.Movie("Avatar", "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/commons/0/09/Female_Avatar_by_Tucia_%28not_from_the_movie%29.jpg",
                     "http://www.youtube.com/watch?v=-9ceBgWV8io", 2009)
school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74", 2003)
ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
                          "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk", 2007)
midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors",
                                "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=dtiklALGz20", 2011)
hunger_games = media.Movie("Hunger Games", "A really real reality show",
                           "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo", 2012)

# define movie list
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

#build movie web page.
fresh_tomatoes.open_movies_page(movies)
