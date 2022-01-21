# current_user_saved_albums(limit=20, offset=0, market=None)

Gets a list of the albums saved in the current authorized user’s “Your Music” library

## Parameters:
- `limit` - the number of albums to return (MAX_LIMIT=50)
- `offset` - the index of the first album to return
- `market` - an ISO 3166-1 alpha-2 country code.

## Sample Response:
```
{
  "href": "https://api.spotify.com/v1/me/albums?offset=0&limit=50", 
  "items": [
    {
      "added_at": "2021-06-10T18:23:22Z", 
      "album": {
        "album_type": "album", 
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6LHsnRBUYhFyt01PdKXAF5"
            }, 
            "href": "https://api.spotify.com/v1/artists/6LHsnRBUYhFyt01PdKXAF5", 
            "id": "6LHsnRBUYhFyt01PdKXAF5", 
            "name": "Bob Moses", 
            "type": "artist", 
            "uri": "spotify:artist:6LHsnRBUYhFyt01PdKXAF5"
          }
        ], 
        "available_markets": [
          "AD", 
          "AE",
          ...
        ], 
        "copyrights": [
          {
            "text": "2015 Domino Recording Co Ltd", 
            "type": "C"
          }, 
          {
            "text": "2015 Domino Recording Co Ltd", 
            "type": "P"
          }
        ], 
        "external_ids": {
          "upc": "887828034062"
        }, 
        "external_urls": {
          "spotify": "https://open.spotify.com/album/0u3Rl4KquP15smujFrgGz4"
        }, 
        "genres": [], 
        "href": "https://api.spotify.com/v1/albums/0u3Rl4KquP15smujFrgGz4", 
        "id": "0u3Rl4KquP15smujFrgGz4", 
        "images": [
          {
            "height": 640, 
            "url": "https://i.scdn.co/image/ab67616d0000b273f27c3660f369422f8a9af4a9", 
            "width": 640
          }, 
          {
            "height": 300, 
            "url": "https://i.scdn.co/image/ab67616d00001e02f27c3660f369422f8a9af4a9", 
            "width": 300
          }, 
          {
            "height": 64, 
            "url": "https://i.scdn.co/image/ab67616d00004851f27c3660f369422f8a9af4a9", 
            "width": 64
          }
        ], 
        "label": "Domino Recording Co", 
        "name": "Days Gone By", 
        "popularity": 56, 
        "release_date": "2015-09-18", 
        "release_date_precision": "day", 
        "total_tracks": 10, 
        "tracks": {
          "href": "https://api.spotify.com/v1/albums/0u3Rl4KquP15smujFrgGz4/tracks?offset=0&limit=50", 
          "items": [
            {
              "artists": [
                {
                  "external_urls": {
                    "spotify": "https://open.spotify.com/artist/6LHsnRBUYhFyt01PdKXAF5"
                  }, 
                  "href": "https://api.spotify.com/v1/artists/6LHsnRBUYhFyt01PdKXAF5", 
                  "id": "6LHsnRBUYhFyt01PdKXAF5", 
                  "name": "Bob Moses", 
                  "type": "artist", 
                  "uri": "spotify:artist:6LHsnRBUYhFyt01PdKXAF5"
                }
              ], 
              "available_markets": [
                "AD", 
                "AE",
                ...
              ], 
              "disc_number": 1, 
              "duration_ms": 380413, 
              "explicit": false, 
              "external_urls": {
                "spotify": "https://open.spotify.com/track/6mnTzibrAUV2vhSjiZo8Tu"
              }, 
              "href": "https://api.spotify.com/v1/tracks/6mnTzibrAUV2vhSjiZo8Tu", 
              "id": "6mnTzibrAUV2vhSjiZo8Tu", 
              "is_local": false, 
              "name": "Like It Or Not", 
              "preview_url": "https://p.scdn.co/mp3-preview/09497d99ffa074b7190ed32e369c36570bee9525?cid=d0241d33ae9f4e79a374ca4109b71f12", 
              "track_number": 1, 
              "type": "track", 
              "uri": "spotify:track:6mnTzibrAUV2vhSjiZo8Tu"
            }, 
            ...
          ], 
          "limit": 50, 
          "next": null, 
          "offset": 0, 
          "previous": null, 
          "total": 10
        }, 
        "type": "album", 
        "uri": "spotify:album:0u3Rl4KquP15smujFrgGz4"
      }
    }
    ...
  ], 
  "limit": 50, 
  "next": "https://api.spotify.com/v1/me/albums?offset=50&limit=50", 
  "offset": 0, 
  "previous": null, 
  "total": 61
}
```