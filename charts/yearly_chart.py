import matplotlib.pyplot as plt
from modules.analytics import MovieAnalytics

def yearly_chart(df, show=True):
    values = MovieAnalytics(df).yearly_summary()
    fig, ax = plt.subplots(figsize=(8, 5))
    if values.empty:
        ax.text(0.5, 0.5, "No data available", ha="center", va="center")
    else:
        values.plot(kind="line", marker="o", ax=ax)
    ax.set_title("Movies by Release Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Movies")
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    if show:
        plt.show()
    return fig
