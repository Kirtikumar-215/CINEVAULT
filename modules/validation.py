from datetime import datetime
from config import STATUSES, GENRES, LANGUAGES

def validate_title(title):
    title = str(title).strip()
    if not title:
        raise ValueError("Movie title cannot be empty.")
    if len(title) > 150:
        raise ValueError("Movie title is too long.")
    return title

def validate_rating(rating):
    try:
        value = float(rating)
    except (TypeError, ValueError) as exc:
        raise ValueError("Rating must be a number.") from exc
    if not 0 <= value <= 5:
        raise ValueError("Rating must be between 0 and 5.")
    return round(value, 1)

def validate_year(year):
    try:
        value = int(year)
    except (TypeError, ValueError) as exc:
        raise ValueError("Year must be a whole number.") from exc
    current_year = datetime.now().year
    if not 1888 <= value <= current_year:
        raise ValueError(f"Year must be between 1888 and {current_year}.")
    return value

def validate_duration(duration):
    try:
        value = int(duration)
    except (TypeError, ValueError) as exc:
        raise ValueError("Duration must be a whole number in minutes.") from exc
    if value <= 0 or value > 1000:
        raise ValueError("Duration must be between 1 and 1000 minutes.")
    return value

def validate_status(status):
    if status not in STATUSES:
        raise ValueError("Invalid viewing status.")
    return status

def validate_choice(value, choices, label):
    if value not in choices:
        raise ValueError(f"Invalid {label}.")
    return value

def validate_movie_data(data):
    return {
        "title": validate_title(data["title"]),
        "genre": validate_choice(data["genre"], GENRES, "genre"),
        "rating": validate_rating(data["rating"]),
        "year": validate_year(data["year"]),
        "language": validate_choice(data["language"], LANGUAGES, "language"),
        "duration": validate_duration(data["duration"]),
        "status": validate_status(data["status"]),
        "favorite": "Yes" if data["favorite"] == "Yes" else "No",
        "date_added": str(data.get("date_added", "")),
        "date_watched": str(data.get("date_watched", "")),
        "notes": str(data.get("notes", "")).strip(),
    }
