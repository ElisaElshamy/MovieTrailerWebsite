import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            color: #FFF;
            background-color: #000;
            width: 100%;
        }
        .container {
            width: 100%;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .genre-row {
            background-color: #403F3F;
            margin-top: 40px;
            width: 100%;
            clear: left;
            float: left;
        }
        .genre {
            background-color: #222;
            overflow: hidden;
            height: 5em;
        }
        .genre h1 {
            margin-left: 20px;
        }
        .movie-tile {
            /*margin-bottom: 20px;
            padding-top: 20px;*/
            margin: 20px 0;
            padding: 0;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .movie_info {
            position: absolute;
            height: 100%;
            background-color: black;
            opacity: 0.7;
            color: white;
            padding: 40px;
            font-size: 18px;
            overflow: auto;
        }
        .storyline {
            text-align: justify;
        }
        .movie_cast {
            font-style: italic;
            text-align: left;
            border-top: 1px dotted white;
            margin-top: 40px;
            padding-top: 10px;
            font-size: 0.8em;
        }
        .cast_list {
            padding: 0;
        }
        .cast_list li {
            display: inline;
        }
        .movie_rating {
            text-align: right;
            font-style: italic;
            font-size: 0.8em;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        $(document).on('mouseover', '.movie-tile', function (event) {
        	$(this).find(".movie_info").show();
        });
        $(document).on('mouseout', '.movie-tile', function (event) {
            $(this).find(".movie_info").hide();
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.genre_row').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {genre_rows}
    </div>
  </body>
</html>
'''

# Genre HTML template
genre_row = '''
<div class="genre-row">
    <div class="genre">
        <h1>{genre}</h1>
    </div>
    {movies_by_genre}
</div>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <div class="movie_info" style="display: none;">
        <p class="storyline">{movie_storyline}</p>
        <div class="movie_cast">{movie_cast}</div>
        <div class="movie_rating">
            <span>{movie_rating}/10</span>
        </div>
    </div>
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''


# Sorts movies by their genre(s)
def movie_by_genre(movies):
    genres = {}

    for movie in movies:
        for genre in movie.genre:
            genres.setdefault(genre, []).append(movie)

    return genres


# Puts movie casting in a nicely formatted list and limits the cast by 6
def movie_casting(movie):
    cast = '''<ul class="cast_list">'''

    for casting in movie.cast[:5]:
        cast += '''<li>''' + str(casting) + ''', </li>'''

    # We do not want the last one to have a comma
    cast = cast + '''<li>''' + str(movie.cast[5]) + '''</li></ul>'''

    return cast


def create_movie_tiles_content(movies_by_genre):
    # The HTML content for this section of the page
    content = ''
    tile_content = ''
    for genre in movies_by_genre:
        for movie in movies_by_genre[genre]:
            # Extract the youtube ID from the url
            youtube_id_match = re.search(
                r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
            youtube_id_match = youtube_id_match or re.search(
                r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
            trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                                  else None)

            cast = movie_casting(movie)
            # Append the tile for the movie with its content filled in
            tile_content += movie_tile_content.format(
                movie_title=movie.title,
                movie_storyline=movie.storyline,
                movie_cast=cast,
                movie_rating=movie.rating,
                poster_image_url=movie.poster_image_url,
                trailer_youtube_id=trailer_youtube_id
            )

        # Displays the movies by their genre
        content += genre_row.format(
            genre=genre,
            movies_by_genre=tile_content)

        # Reset for next genre iteration
        tile_content = ''
        cast = ''

    return content


def open_movies_page(movies_by_genre):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        # movie_tiles=create_movie_tiles_content(movies_by_genre))
        genre_rows=create_movie_tiles_content(movies_by_genre))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
