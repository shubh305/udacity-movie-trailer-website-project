import fresh_tomatoes
import media

# Initialize some list of movies to be rendered, and put them in a list.

predestination = media.Movie("Predestination",
                              "To save the future he must reshape the past.",
                              "https://upload.wikimedia.org/wikipedia/en/4/4b/Predestination_poster.jpg",  # noqa
                              "https://www.youtube.com/watch?v=UVOpfpYijHA", "2014")  # noqa

maze_runner = media.Movie("The Maze Runner",
                           "They're all trapped in a maze to escape.",
                           "https://upload.wikimedia.org/wikipedia/en/b/be/The_Maze_Runner_poster.jpg",  # noqa
                           "https://www.youtube.com/watch?v=64-iSYVmMVY", "2014")  # noqa

la_la_land = media.Movie("La La Land",
                          "A jazz pianist falls for an actress in Los Angeles. ", "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",  # noqa
                          "https://www.youtube.com/watch?v=0pdqf4P9MB8", "2014")  # noqa

edge_of_tomorrow = media.Movie("Edge of Tomorrow",
                                '''A soldier fighting aliens gets to relive the
                                 same day over and over again,
                                the day restarting every time he dies.''',
                                "https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",  # noqa
                                "https://www.youtube.com/watch?v=yUmSVcttXnI", "2014")  # noqa

saw = media.Movie("Saw", "Every piece has a puzzle.",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BMjE4MDYzNDE1OV5BMl5BanBnXkFtZTcwNDY2OTYwNA@@._V1_QL50_SY1000_SX675_AL_.jpg",  # noqa
                   "https://www.youtube.com/watch?v=S-1QgOMQ-ls", "2014")

moonlight = media.Movie("Moonlight",
                         '''A chronicle of the childhood, adolescence
                         and burgeoning adulthood of a young black man.''', "https://upload.wikimedia.org/wikipedia/en/8/84/Moonlight_%282016_film%29.png",  # noqa
                         "https://www.youtube.com/watch?v=9NJj12tJzqc", "2014")  # noqa

# Create a movie array to contain list of movies
movies = [predestination, maze_runner, la_la_land,
          edge_of_tomorrow, saw, moonlight]

# Open the list of movies in the webpage
fresh_tomatoes.open_movies_page(movies)
