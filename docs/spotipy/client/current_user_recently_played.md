# current_user_recently_played(limit=50, after=None, before=None)

Get the current user’s recently played tracks

## Parameters:
- `limit` - the number of entities to return
- `after` - unix timestamp in milliseconds. Returns all items after (but not including) this cursor position. Cannot be used if before is specified.
- `before` - unix timestamp in milliseconds. Returns all items before (but not including) this cursor position. Cannot be used if after is specified

## Sample Response
```
{
  "cursors": {
    "after": "1642794480816", 
    "before": "1642787621567"
  }, 
  "href": "https://api.spotify.com/v1/me/player/recently-played?limit=50", 
  "items": [
    {
      "context": {
        "external_urls": {
          "spotify": "https://open.spotify.com/playlist/0vvXsWCC9xrXsKd4FyS8kM"
        }, 
        "href": "https://api.spotify.com/v1/playlists/0vvXsWCC9xrXsKd4FyS8kM", 
        "type": "playlist", 
        "uri": "spotify:playlist:0vvXsWCC9xrXsKd4FyS8kM"
      }, 
      "played_at": "2022-01-21T17:53:41.567Z", 
      "track": {
        "album": {
          "album_type": "album", 
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4XbnhifKeOnyfTsCInrQsX"
              }, 
              "href": "https://api.spotify.com/v1/artists/4XbnhifKeOnyfTsCInrQsX", 
              "id": "4XbnhifKeOnyfTsCInrQsX", 
              "name": "No Spirit", 
              "type": "artist", 
              "uri": "spotify:artist:4XbnhifKeOnyfTsCInrQsX"
            }
          ], 
          "available_markets": [
            "AD", 
            "AE",
            ...
          ], 
          "external_urls": {
            "spotify": "https://open.spotify.com/album/1q1XyQlquRzBDmkQUeHUP5"
          }, 
          "href": "https://api.spotify.com/v1/albums/1q1XyQlquRzBDmkQUeHUP5", 
          "id": "1q1XyQlquRzBDmkQUeHUP5", 
          "images": [
            {
              "height": 640, 
              "url": "https://i.scdn.co/image/ab67616d0000b273d505530ab454cf9bedd0866e", 
              "width": 640
            }, 
            {
              "height": 300, 
              "url": "https://i.scdn.co/image/ab67616d00001e02d505530ab454cf9bedd0866e", 
              "width": 300
            }, 
            {
              "height": 64, 
              "url": "https://i.scdn.co/image/ab67616d00004851d505530ab454cf9bedd0866e", 
              "width": 64
            }
          ], 
          "name": "Happy Moments", 
          "release_date": "2021-11-12", 
          "release_date_precision": "day", 
          "total_tracks": 12, 
          "type": "album", 
          "uri": "spotify:album:1q1XyQlquRzBDmkQUeHUP5"
        }, 
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4XbnhifKeOnyfTsCInrQsX"
            }, 
            "href": "https://api.spotify.com/v1/artists/4XbnhifKeOnyfTsCInrQsX", 
            "id": "4XbnhifKeOnyfTsCInrQsX", 
            "name": "No Spirit", 
            "type": "artist", 
            "uri": "spotify:artist:4XbnhifKeOnyfTsCInrQsX"
          }, 
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4tQMVafcBzEyxZqY81q3Fj"
            }, 
            "href": "https://api.spotify.com/v1/artists/4tQMVafcBzEyxZqY81q3Fj", 
            "id": "4tQMVafcBzEyxZqY81q3Fj", 
            "name": "Tonion", 
            "type": "artist", 
            "uri": "spotify:artist:4tQMVafcBzEyxZqY81q3Fj"
          }
        ], 
        "available_markets": [
          "AD", 
          "AE",
          ...
        ], 
        "disc_number": 1, 
        "duration_ms": 200281, 
        "explicit": false, 
        "external_ids": {
          "isrc": "GBLV62118096"
        }, 
        "external_urls": {
          "spotify": "https://open.spotify.com/track/7KMILxJFhcSs2LH5JrrZMy"
        }, 
        "href": "https://api.spotify.com/v1/tracks/7KMILxJFhcSs2LH5JrrZMy", 
        "id": "7KMILxJFhcSs2LH5JrrZMy", 
        "is_local": false, 
        "name": "Running Out Of Time", 
        "popularity": 50, 
        "preview_url": "https://p.scdn.co/mp3-preview/2d012f86a5fa09e1b076b8a55519c2a262d7d858?cid=d0241d33ae9f4e79a374ca4109b71f12", 
        "track_number": 2, 
        "type": "track", 
        "uri": "spotify:track:7KMILxJFhcSs2LH5JrrZMy"
      }
    }
    ...
  ], 
  "limit": 50, 
  "next": "https://api.spotify.com/v1/me/player/recently-played?before=1642787621567&limit=50"
}
```