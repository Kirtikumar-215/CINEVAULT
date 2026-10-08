import pandas as pd
from modules.analytics import MovieAnalytics

def sample():
    return pd.DataFrame([
        {"id": 1, "title": "A", "genre": "Action", "rating": 5, "year": 2025,
         "language": "English", "duration": 120, "status": "Watched", "favorite": "Yes"},
        {"id": 2, "title": "B", "genre": "Comedy", "rating": 3, "year": 2026,
         "language": "Hindi", "duration": 100, "status": "Plan to Watch", "favorite": "No"},
    ])

def test_total():
    assert MovieAnalytics(sample()).total_movies() == 2

def test_average():
    assert MovieAnalytics(sample()).average_rating() == 4

def test_preferred_genre():
    assert MovieAnalytics(sample()).preferred_genre() == "Action"

def test_watched_percentage():
    assert MovieAnalytics(sample()).watched_percentage() == 50.0
