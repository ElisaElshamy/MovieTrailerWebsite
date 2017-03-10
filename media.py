import webbrowser


# Defining Movie class and it's properties
class Movie():

    def __init__(self, movie_title, movie_storyline, movie_genre, movie_cast,
                 movie_rating, poster_image, trailer_youtube):

        self.title = movie_title
        self.storyline = movie_storyline
        self.genre = movie_genre
        self.cast = movie_cast
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # Opens YouTube movie trailer using URL
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
