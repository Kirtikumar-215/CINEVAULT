import matplotlib.pyplot as plt
from modules.analytics import MovieAnalytics

def genre_chart(df, show=True):
    values = MovieAnalytics(df).genre_summary()
    fig, ax = plt.subplots(figsize=(8, 5))
    if values.empty:
        ax.text(0.5, 0.5, "No data available", ha="center", va="center")
    else:
        values.plot(kind="bar", ax=ax)
    ax.set_title("Movie Collection by Genre")
    ax.set_xlabel("Genre")
    ax.set_ylabel("Number of Movies")
    fig.tight_layout()
    if show:
        plt.show()
    return fig
