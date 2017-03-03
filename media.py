import webbrowser


class Movie():

    # A data structure to store the movies and their required details
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = movie_release_date

    # A data structure to open the trailer when click on the poster
    def show_trailer(self):
        webbrowser.open(self.trailer)
