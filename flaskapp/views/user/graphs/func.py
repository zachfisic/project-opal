import pandas as pd



def create_top_artists_dataframe(spotify, time_range="long_term", limit=20):
    """Generates a Pandas Dataframe of top artists for a user.

    Selects a user's top artists in a given time window and normalizes the response into a dataframe before returning the result.

    Args:
        spotify: an authorized instance of Spotify
        time_range: the range to consider for the query
        limit: the maximum number of items to return for every `time_range`

    Returns:
        A dataframe of artists labeled with the Spotify response
    """

    allowed_ranges = ["short_term", "medium_term", "long_term"]
    if time_range in allowed_ranges:
        return pd.json_normalize(spotify.current_user_top_artists(time_range=time_range, limit=limit)['items'])
    elif time_range == "all":
        artists = pd.DataFrame()
        for t in allowed_ranges:
            df = pd.json_normalize(spotify.current_user_top_artists(time_range=t, limit=limit)['items'])
            artists = artists.append(df)
        return artists



def create_related_artists_dataframe(spotify, artist_id, limit=5):
    """Generate a Pandas Dataframe of related artists from a given artist id"""

    return pd.json_normalize(spotify.artist_related_artists(artist_id)['artists'][:limit])