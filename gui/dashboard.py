import tkinter as tk
from tkinter import messagebox

from modules.movie_manager import MovieManager
from modules.analytics import MovieAnalytics
from modules.recommendations import get_recommendations
from gui.widgets import make_card
from gui.movie_collection import MovieCollectionView
from gui.analytics_view import AnalyticsView
from gui.preferences_view import PreferencesView
from gui.reports_view import ReportsView

class CineVaultApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CineVault — Movie Collection & Preference Analyzer")
        self.geometry("1250x780")
        self.minsize(1050, 700)
        self.configure(bg="#0f1725")
        self.manager = MovieManager()
        self.current_view = None
        self.sidebar()
        self.content = tk.Frame(self, bg="#0f1725")
        self.content.pack(side="right", fill="both", expand=True)
        self.show_dashboard()

    def sidebar(self):
        side = tk.Frame(self, bg="#111a2b", width=210)
        side.pack(side="left", fill="y")
        side.pack_propagate(False)
        tk.Label(side, text="🎬", bg="#111a2b", fg="white",
                 font=("Segoe UI Emoji", 30)).pack(pady=(30, 0))
        tk.Label(side, text="CineVault", bg="#111a2b", fg="white",
                 font=("Segoe UI", 20, "bold")).pack()
        tk.Label(side, text="Movie Intelligence", bg="#111a2b", fg="#7185a5",
                 font=("Segoe UI", 8)).pack(pady=(0, 30))
        buttons = [
            ("⌂  Dashboard", self.show_dashboard),
            ("▣  Movie Collection", self.show_movies),
            ("＋  Add Movie", self.add_movie),
            ("◈  Analytics", self.show_analytics),
            ("♥  Preferences", self.show_preferences),
            ("▥  Reports", self.show_reports),
        ]
        for text, command in buttons:
            tk.Button(side, text=text, command=command, anchor="w",
                      bg="#111a2b", fg="#b9c7dc", activebackground="#26344d",
                      activeforeground="white", relief="flat", bd=0,
                      font=("Segoe UI", 10, "bold"), padx=24, pady=12).pack(fill="x")
        tk.Label(side, text="Python • Tkinter • Pandas\nNumPy • Matplotlib • CSV",
                 bg="#111a2b", fg="#536783", font=("Segoe UI", 8),
                 justify="left").pack(side="bottom", anchor="w", padx=22, pady=22)

    def clear(self):
        for child in self.content.winfo_children():
            child.destroy()

    def show_dashboard(self):
        self.clear()
        frame = tk.Frame(self.content, bg="#0f1725")
        frame.pack(fill="both", expand=True, padx=28, pady=28)
        analytics = MovieAnalytics(self.manager.get_all_movies())
        tk.Label(frame, text="Good evening 👋", bg="#0f1725", fg="#7588a8",
                 font=("Segoe UI", 11)).pack(anchor="w")
        tk.Label(frame, text="Your Movie Dashboard", bg="#0f1725", fg="white",
                 font=("Segoe UI", 27, "bold")).pack(anchor="w", pady=(2, 22))
        cards = tk.Frame(frame, bg="#0f1725")
        cards.pack(fill="x")
        values = [
            ("TOTAL MOVIES", analytics.total_movies(), "in your collection"),
            ("WATCHED", analytics.watched_count(), f"{analytics.watched_percentage()}% completed"),
            ("AVG RATING", f"{analytics.average_rating():.1f} ★", "out of 5"),
            ("TOP GENRE", analytics.preferred_genre(), "most collected"),
        ]
        for title, value, subtitle in values:
            make_card(cards, title, value, subtitle).pack(side="left", padx=(0, 12))

        lower = tk.Frame(frame, bg="#0f1725")
        lower.pack(fill="both", expand=True, pady=24)
        left = tk.Frame(lower, bg="#172033")
        left.pack(side="left", fill="both", expand=True, padx=(0, 12))
        tk.Label(left, text="Taste Snapshot", bg="#172033", fg="white",
                 font=("Segoe UI", 15, "bold")).pack(anchor="w", padx=20, pady=(20, 8))
        tk.Label(left, text=analytics.preference_summary(), bg="#172033", fg="#9eb0cb",
                 wraplength=500, justify="left", font=("Segoe UI", 10)).pack(anchor="w", padx=20)
        tags = ", ".join(analytics.genre_summary().head(3).index.tolist()) if not self.manager.get_all_movies().empty else "—"
        tk.Label(left, text=f"\nTop genres: {tags}", bg="#172033", fg="#d7e0ef",
                 font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=20)

        right = tk.Frame(lower, bg="#172033")
        right.pack(side="right", fill="both", expand=True)
        tk.Label(right, text="Suggested From Your Collection", bg="#172033", fg="white",
                 font=("Segoe UI", 15, "bold")).pack(anchor="w", padx=20, pady=(20, 8))
        recs = get_recommendations(self.manager.get_all_movies())
        for title in recs or ["Add more movies to unlock suggestions."]:
            tk.Label(right, text=f"• {title}", bg="#172033", fg="#aebbd0",
                     font=("Segoe UI", 10)).pack(anchor="w", padx=20, pady=3)

    def show_movies(self):
        self.clear()
        self.current_view = MovieCollectionView(
            self.content, self.manager, on_change=self.refresh_all
        )
        self.current_view.pack(fill="both", expand=True)

    def add_movie(self):
        if self.current_view and isinstance(self.current_view, MovieCollectionView):
            self.current_view.add_movie()
        else:
            self.show_movies()
            self.after(100, self.current_view.add_movie)

    def show_analytics(self):
        self.clear()
        self.current_view = AnalyticsView(self.content, self.manager)
        self.current_view.pack(fill="both", expand=True)

    def show_preferences(self):
        self.clear()
        self.current_view = PreferencesView(self.content, self.manager)
        self.current_view.pack(fill="both", expand=True)

    def show_reports(self):
        self.clear()
        self.current_view = ReportsView(self.content, self.manager)
        self.current_view.pack(fill="both", expand=True)

    def refresh_all(self):
        self.manager.refresh()
        if isinstance(self.current_view, MovieCollectionView):
            self.current_view.refresh()
