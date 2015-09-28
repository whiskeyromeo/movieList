import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_url, movie_director, release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_url
        self.director = movie_director
        self.release_date = release_date
    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
