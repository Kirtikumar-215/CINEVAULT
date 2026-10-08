import pandas as pd
from modules.movie_manager import MovieManager

def test_search_movies():
    manager = MovieManager()
    result = manager.search_movies("Interstellar")
    assert "Interstellar" in result["title"].tolist()

def test_filter_genre():
    manager = MovieManager()
    result = manager.filter_movies(genre="Sci-Fi")
    assert all(result["genre"] == "Sci-Fi")
