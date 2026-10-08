from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
BACKUP_DIR = DATA_DIR / "backup"
REPORT_DIR = BASE_DIR / "reports" / "generated"
DATA_FILE = DATA_DIR / "movies.csv"

DATA_DIR.mkdir(exist_ok=True)
BACKUP_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

STATUSES = ["Watched", "Watching", "Plan to Watch"]
GENRES = [
    "Action", "Adventure", "Animation", "Comedy", "Crime", "Drama",
    "Fantasy", "Horror", "Mystery", "Romance", "Sci-Fi", "Thriller",
    "Documentary", "Other"
]
LANGUAGES = ["English", "Hindi", "Gujarati", "Tamil", "Telugu", "Malayalam", "Other"]
