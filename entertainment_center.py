import fresh_tomatoes
import media
import sys

reload(sys)

# Some movie titles have characters from languages other than English
sys.setdefaultencoding('utf-8')

# Include the IMDbPY API
sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/IMDbPY-5.1.1-py2.7-macosx-10.6-intel.egg")  # NOQA
sys.path.append("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/lxml-3.7.2-py2.7-macosx-10.6-intel.egg")  # NOQA

from imdb import IMDb

ia = IMDb()

# Eternal Sunshine of the Spotless Mind
imdb_data = ia.get_movie('0338013')
ESOTSM = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
    imdb_data['cast'],
    imdb_data['rating'],
    "https://infinitecrescendo.files.wordpress.com/2014/03/eternal-sunshine-of-the-spotless-mind-poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=0zFywiAh7N0")

# The Science of Sleep
imdb_data = ia.get_movie('0354899')
TSOS = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
    imdb_data['cast'],
    imdb_data['rating'],
    "https://i.jeded.com/i/the-science-of-sleep-la-science-des-rves.10619.jpg",  # NOQA
    "https://www.youtube.com/watch?v=oJ8VWoyMJoc")

# Equilibrium
imdb_data = ia.get_movie('0238380')
Equilibrium = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "http://fontmeme.com/images/equilibrium-alt-movie-poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=raleKODYeg0")

# Sucker Punch
imdb_data = ia.get_movie('0978764')
Sucker_Punch = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "http://www.warnerbros.com/sites/default/files/suckerpunch_keyart.jpg",  # NOQA
    "https://www.youtube.com/watch?v=MnF4SpS9gUw")

# Oblivion
imdb_data = ia.get_movie('1483013')
Oblivion = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "http://cdn.collider.com/wp-content/uploads/oblivion-poster-morgan-freeman-tom-cruise.jpg",  # NOQA
    "https://www.youtube.com/watch?v=w0qQkSuWOS8")

# Interstellar
imdb_data = ia.get_movie('0816692')
Interstellar = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UY1200_CR69,0,630,1200_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=0vxOhd4qlnA")

# Shutter Island
imdb_data = ia.get_movie('1130884')
Shutter_Island = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxMTIyNzMxMV5BMl5BanBnXkFtZTcwOTc4OTI3Mg@@._V1_UY1200_CR83,0,630,1200_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=5iaYLCiq5RM")

# The Butterfly Effect
imdb_data = ia.get_movie('0289879')
The_Butterfly_Effect = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "http://content7.flixster.com/movie/11/16/99/11169913_ori.jpg",  # NOQA
    "https://www.youtube.com/watch?v=B8_dgqfPXFg")

# Slumdog Millionaire
imdb_data = ia.get_movie('1010048')
Slumdog_Millionaire = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU2NTA5NzI0N15BMl5BanBnXkFtZTcwMjUxMjYxMg@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=AIzbwV7on6Q")

# O (Othello)
imdb_data = ia.get_movie('0184791')
O = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "http://www.joblo.com/timthumb.php?src=/posters/images/full/o-movie-poster.jpg&h=600&q=100",  # NOQA
    "https://www.youtube.com/watch?v=Bz1NIOjkJi0")

# Romeo + Juliet
imdb_data = ia.get_movie('0117509')
Romeo_Juliet = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "https://literaryundertakings.files.wordpress.com/2015/04/romeo-the-perfect-romeo-and-juliet-3-30505957-1012-1438-1mjxbb2.jpg",  # NOQA
    "https://www.youtube.com/watch?v=gjxHdNxvySU")

# Black Swan
imdb_data = ia.get_movie('0947798')
Black_Swan = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNzY2NzI4OTE5MF5BMl5BanBnXkFtZTcwMjMyNDY4Mw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=5jaI1XOB-bs")

# Carrie
imdb_data = ia.get_movie('0074285')
Carrie = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "https://nighthawknews.files.wordpress.com/2015/12/carrie-1976-movie-poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=VSF6WVx_Tdo")

# RoboCop
imdb_data = ia.get_movie('0093870')
Robocop = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "http://www.theterminatorfans.com/wp-content/uploads/2013/09/RoboCop-1987-Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=zbCbwP6ibR4")

# Elysium
imdb_data = ia.get_movie('1535108')
Elysium = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "http://cdn.collider.com/wp-content/uploads/Elysium-poster2.jpg",  # NOQA
    "https://www.youtube.com/watch?v=QILNSgou5BY")

# Maleficent
imdb_data = ia.get_movie('1587310')
Maleficent = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "http://vignette1.wikia.nocookie.net/disney/images/a/a4/Maleficent-(2014)-149.jpg/revision/latest?cb=20140419102200",  # NOQA
    "https://www.youtube.com/watch?v=w-XO4XiRop0")

# Wanted
imdb_data = ia.get_movie('0493464')
Wanted = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "http://image.tmdb.org/t/p/original/wiMo2FCDSvpqDuWB2sb3GX2MW8W.jpg",  # NOQA
    "https://www.youtube.com/watch?v=q9Mr-iYZRZk")

# Gremlins
imdb_data = ia.get_movie('0087363')
Gremlins = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "http://www.nerdspan.com/wp-content/uploads/2013/12/Gremlins-Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=-14d51QTVjo")

# Human Centipede
imdb_data = ia.get_movie('1467304')
Human_Centipede = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "http://ia.media-imdb.com/images/M/MV5BMTY4Nzk3NzYxOF5BMl5BanBnXkFtZTcwODQwNjQzMw@@._V1_UY1200_CR92,0,630,1200_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=IX8fKLjC__c")

# KungFu Panda
imdb_data = ia.get_movie('0441773')
KungFu_Panda = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "http://www.impawards.com/2008/posters/kung_fu_panda.jpg",  # NOQA
    "https://www.youtube.com/watch?v=PXi3Mv6KMzY")

# The Departed
imdb_data = ia.get_movie('0407887')
The_Departed = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "http://moviefiles.alphacoders.com/424/poster-424.jpg",  # NOQA
    "https://www.youtube.com/watch?v=SGWvwjZ0eDc")

# Catch Me if You Can
imdb_data = ia.get_movie('0264464')
CMIYC = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "https://www.movieposter.com/posters/archive/main/6/MPW-3247",  # NOQA
    "https://www.youtube.com/watch?v=71rDQ7z4eFg")

# Black Mass
imdb_data = ia.get_movie('1355683')
Black_Mass = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNzg0ODI3NDQxNF5BMl5BanBnXkFtZTgwMzgzNDA0NjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=CE3e3hGF2jc")

# A Bronx Tale
imdb_data = ia.get_movie('0106489')
ABT = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "http://cdn.collider.com/wp-content/uploads/2016/06/a-bronx-tale-poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=z50PjmZYS4A")

# Ever After
imdb_data = ia.get_movie('0120631')
Ever_After = media.Movie(
    imdb_data['title'],
    imdb_data['plot'][0],
    imdb_data['genres'],
            imdb_data['cast'],
            imdb_data['rating'],
    "http://www.everaftercostumes.com/gold/poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=Hcj9fyx6DXI")


movies = [
    ESOTSM,
    TSOS,
    Equilibrium,
    Sucker_Punch,
    Oblivion,
    Interstellar,
    Shutter_Island,
    The_Butterfly_Effect,
    Slumdog_Millionaire,
    O,
    Romeo_Juliet,
    Black_Swan,
    Carrie,
    Robocop,
    Elysium,
    Maleficent,
    Wanted,
    Gremlins,
    Human_Centipede,
    KungFu_Panda,
    The_Departed,
    CMIYC,
    Black_Mass,
    ABT,
    Ever_After]

# Sort movies by genre
genres = fresh_tomatoes.movie_by_genre(movies)

# Open the HTML page
fresh_tomatoes.open_movies_page(genres)
