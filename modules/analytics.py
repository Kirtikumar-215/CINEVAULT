import numpy as np
import pandas as pd

class MovieAnalytics:
    def __init__(self, df):
        self.df = df.copy()
        defaults = {
            "genre": "",
            "status": "",
            "language": "",
            "rating": 0.0,
            "year": 0,
            "favorite": "No",
        }
        for column, default in defaults.items():
            if column not in self.df:
                self.df[column] = default

    def total_movies(self):
        return len(self.df)

    def watched_count(self):
        return int((self.df["status"] == "Watched").sum())

    def watching_count(self):
        return int((self.df["status"] == "Watching").sum())

    def plan_count(self):
        return int((self.df["status"] == "Plan to Watch").sum())

    def average_rating(self):
        return round(float(np.mean(self.df["rating"])) if not self.df.empty else 0, 2)

    def highest_rating(self):
        return float(np.max(self.df["rating"])) if not self.df.empty else 0

    def lowest_rating(self):
        return float(np.min(self.df["rating"])) if not self.df.empty else 0

    def favorite_count(self):
        return int((self.df["favorite"] == "Yes").sum())

    def genre_summary(self):
        return self.df["genre"].value_counts()

    def status_summary(self):
        return self.df["status"].value_counts()

    def language_summary(self):
        return self.df["language"].value_counts()

    def rating_summary(self):
        return self.df["rating"].round().value_counts().sort_index()

    def average_rating_by_genre(self):
        return self.df.groupby("genre")["rating"].mean().round(2).sort_values(ascending=False)

    def preferred_genre(self):
        summary = self.genre_summary()
        return str(summary.index[0]) if not summary.empty else "No data"

    def preferred_language(self):
        summary = self.language_summary()
        return str(summary.index[0]) if not summary.empty else "No data"

    def highest_rated_movies(self, limit=5):
        return self.df.sort_values("rating", ascending=False).head(limit)

    def yearly_summary(self):
        if self.df.empty:
            return pd.Series(dtype=int)
        return self.df.groupby("year").size().sort_index()

    def watched_percentage(self):
        return round(self.watched_count() / self.total_movies() * 100, 1) if self.total_movies() else 0

    def compare_periods(self, year1, year2):
        result = {}
        for year in [year1, year2]:
            subset = self.df[self.df["year"] == int(year)]
            result[year] = {
                "movies": len(subset),
                "watched": int((subset["status"] == "Watched").sum()),
                "average_rating": round(float(subset["rating"].mean()), 2) if not subset.empty else 0,
                "favorite_genre": str(subset["genre"].mode().iloc[0]) if not subset.empty else "N/A",
            }
        return result

    def preference_summary(self):
        if self.df.empty:
            return "Add some movies to discover your viewing preferences."
        genre = self.preferred_genre()
        language = self.preferred_language()
        avg = self.average_rating()
        return (
            f"You mostly collect {genre} movies in {language}. "
            f"Your average rating is {avg}/5, and {self.watched_percentage()}% "
            f"of your collection is watched."
        )
