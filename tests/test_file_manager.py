import pandas as pd
from modules.file_manager import save_movies, load_movies

def test_save_and_load(tmp_path):
    path = tmp_path / "movies.csv"
    df = pd.DataFrame([{
        "id": 1, "title": "Test", "genre": "Drama", "rating": 4,
        "year": 2025, "language": "English", "duration": 100,
        "status": "Watched", "favorite": "No", "date_added": "2026-01-01",
        "date_watched": "", "notes": ""
    }])
    save_movies(df, path)
    loaded = load_movies(path)
    assert loaded.iloc[0]["title"] == "Test"
