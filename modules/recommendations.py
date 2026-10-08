from modules.analytics import MovieAnalytics

def get_recommendations(df, limit=5):
    if df.empty:
        return []
    analytics = MovieAnalytics(df)
    preferred = set(analytics.genre_summary().head(3).index.tolist())
    candidates = df[
        df["genre"].isin(preferred) &
        (df["status"] != "Watched")
    ].sort_values(["favorite", "rating"], ascending=[False, False])
    return candidates.head(limit)["title"].tolist()

def get_preference_tags(df):
    if df.empty:
        return []
    analytics = MovieAnalytics(df)
    tags = list(analytics.genre_summary().head(3).index)
    return [str(tag) for tag in tags]
