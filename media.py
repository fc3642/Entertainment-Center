# import the required file for this program
import webbrowser

class Movie():
    """This is the classes provides a way to store movie relateted information."""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    # define the class initiator, The movie title, story line, movie poster link, you tube tailer link and the year produced are the required parameters
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, year):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = year

    # define the method to show movie trailer.
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)

    # define the method to show movie poster image
    def showImage(self):
        webbrowser.open(self.poster_image_url)
