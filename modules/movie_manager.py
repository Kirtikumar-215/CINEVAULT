from datetime import date
import pandas as pd

from modules.file_manager import load_movies, save_movies, create_backup
from modules.validation import validate_movie_data

class MovieManager:
    def __init__(self):
        self.df = load_movies()
        self._normalize()

    def _normalize(self):
        if self.df.empty:
            return
        self.df["id"] = pd.to_numeric(self.df["id"], errors="coerce").fillna(0).astype(int)
        self.df["rating"] = pd.to_numeric(self.df["rating"], errors="coerce").fillna(0.0)
        self.df["year"] = pd.to_numeric(self.df["year"], errors="coerce").fillna(2000).astype(int)
        self.df["duration"] = pd.to_numeric(self.df["duration"], errors="coerce").fillna(1).astype(int)
        self.df["title"] = self.df["title"].fillna("").astype(str)

    def refresh(self):
        self.df = load_movies()
        self._normalize()

    def _next_id(self):
        return int(self.df["id"].max()) + 1 if not self.df.empty else 1

    def add_movie(self, data):
        clean = validate_movie_data(data)
        clean.update({
            "id": self._next_id(),
            "date_added": clean["date_added"] or str(date.today()),
        })
        self.df = pd.concat([self.df, pd.DataFrame([clean])], ignore_index=True)
        save_movies(self.df)
        return int(clean["id"])

    def update_movie(self, movie_id, data):
        clean = validate_movie_data(data)
        matches = self.df.index[self.df["id"] == int(movie_id)].tolist()
        if not matches:
            raise ValueError("Movie not found.")
        idx = matches[0]
        if not clean["date_added"]:
            clean["date_added"] = self.df.at[idx, "date_added"]
        if clean["status"] == "Watched" and not clean["date_watched"]:
            clean["date_watched"] = str(date.today())
        self.df.loc[idx, list(clean.keys())] = list(clean.values())
        save_movies(self.df)
        return True

    def delete_movie(self, movie_id):
        matches = self.df.index[self.df["id"] == int(movie_id)].tolist()
        if not matches:
            raise ValueError("Movie not found.")
        create_backup()
        self.df = self.df.drop(matches[0]).reset_index(drop=True)
        save_movies(self.df)

    def get_movie(self, movie_id):
        matches = self.df[self.df["id"] == int(movie_id)]
        if matches.empty:
            return None
        return matches.iloc[0].to_dict()

    def get_all_movies(self):
        return self.df.copy()

    def search_movies(self, query):
        query = str(query).strip().lower()
        if not query:
            return self.df.copy()
        mask = (
            self.df["title"].astype(str).str.lower().str.contains(query, na=False) |
            self.df["genre"].astype(str).str.lower().str.contains(query, na=False) |
            self.df["language"].astype(str).str.lower().str.contains(query, na=False)
        )
        return self.df[mask].copy()

    def filter_movies(self, genre="All", status="All", language="All",
                      min_rating=0, favorite="All"):
        result = self.df.copy()
        if genre != "All":
            result = result[result["genre"] == genre]
        if status != "All":
            result = result[result["status"] == status]
        if language != "All":
            result = result[result["language"] == language]
        if favorite != "All":
            result = result[result["favorite"] == favorite]
        result = result[result["rating"] >= float(min_rating)]
        return result

    def sort_movies(self, column="title", ascending=True):
        if column not in self.df.columns:
            return self.df.copy()
        return self.df.sort_values(column, ascending=ascending).copy()
