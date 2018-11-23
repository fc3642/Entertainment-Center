# import the required file for this program
import webbrowser


class Movie():
    """Is the classes provides a way to store movie relateted information."""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube, year):
        """Defines the class initiator.

        The movie title, story line, movie poster link, you tube tailer link
        and the year produced are the required parameters.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.year = year

    def showTrailer(self):
        """Defines the method to show movie trailer. """
        webbrowser.open(self.trailer_youtube_url)

    def showImage(self):
        """Defines the method to show movie poster image. """
        webbrowser.open(self.poster_image_url)
