import shutil
from datetime import datetime
from pathlib import Path
import pandas as pd

from config import DATA_FILE, BACKUP_DIR

COLUMNS = [
    "id", "title", "genre", "rating", "year", "language", "duration",
    "status", "favorite", "date_added", "date_watched", "notes"
]

def load_movies(path=DATA_FILE):
    path = Path(path)
    if not path.exists():
        return pd.DataFrame(columns=COLUMNS)
    try:
        df = pd.read_csv(path)
        for col in COLUMNS:
            if col not in df.columns:
                df[col] = ""
        return df[COLUMNS]
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=COLUMNS)
    except (OSError, pd.errors.ParserError) as exc:
        raise ValueError(f"Unable to read movie data: {exc}") from exc

def save_movies(df, path=DATA_FILE):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        df.to_csv(path, index=False)
    except OSError as exc:
        raise ValueError(f"Unable to save movie data: {exc}") from exc

def create_backup(path=DATA_FILE):
    path = Path(path)
    if not path.exists():
        return None
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = BACKUP_DIR / f"movies_{timestamp}.csv"
    shutil.copy2(path, backup)
    return backup

def restore_backup(backup_path, path=DATA_FILE):
    backup_path = Path(backup_path)
    if not backup_path.exists():
        raise FileNotFoundError("Backup file was not found.")
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(backup_path, path)
