# current_playback(market=None, additional_types=None)

Get information about user’s current playback.

## Parameters:
- `market` - an ISO 3166-1 alpha-2 country code.
- `additional_types` - episode to get podcast track information

## Sample Response:

```
{
  "actions": {
    "disallows": {
      "resuming": true
    }
  }, 
  "context": {
    "external_urls": {
      "spotify": "https://open.spotify.com/playlist/0vvXsWCC9xrXsKd4FyS8kM"
    }, 
    "href": "https://api.spotify.com/v1/playlists/0vvXsWCC9xrXsKd4FyS8kM", 
    "type": "playlist", 
    "uri": "spotify:playlist:0vvXsWCC9xrXsKd4FyS8kM"
  }, 
  "currently_playing_type": "track", 
  "device": {
    "id": "5d6b706c36f97db5ed9abe2aa7a40546b5f81f81", 
    "is_active": true, 
    "is_private_session": false, 
    "is_restricted": false, 
    "name": "Zachary\u2019s MacBook Pro", 
    "type": "Computer", 
    "volume_percent": 34
  }, 
  "is_playing": true, 
  "item": {
    "album": {
      "album_type": "album", 
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/6ysKfYgiKUTMCuq2fSTLK3"
          }, 
          "href": "https://api.spotify.com/v1/artists/6ysKfYgiKUTMCuq2fSTLK3", 
          "id": "6ysKfYgiKUTMCuq2fSTLK3", 
          "name": "xander.", 
          "type": "artist", 
          "uri": "spotify:artist:6ysKfYgiKUTMCuq2fSTLK3"
        }
      ], 
      "available_markets": [
        "AD", 
        "AE",
        ...
      ], 
      "external_urls": {
        "spotify": "https://open.spotify.com/album/38rprRSWLTehdqR0Kx50jj"
      }, 
      "href": "https://api.spotify.com/v1/albums/38rprRSWLTehdqR0Kx50jj", 
      "id": "38rprRSWLTehdqR0Kx50jj", 
      "images": [
        {
          "height": 640, 
          "url": "https://i.scdn.co/image/ab67616d0000b273bdbcc151a39d45dde23bb2eb", 
          "width": 640
        }, 
        {
          "height": 300, 
          "url": "https://i.scdn.co/image/ab67616d00001e02bdbcc151a39d45dde23bb2eb", 
          "width": 300
        }, 
        {
          "height": 64, 
          "url": "https://i.scdn.co/image/ab67616d00004851bdbcc151a39d45dde23bb2eb", 
          "width": 64
        }
      ], 
      "name": "Cabin Fever, Pt. 2", 
      "release_date": "2021-10-17", 
      "release_date_precision": "day", 
      "total_tracks": 10, 
      "type": "album", 
      "uri": "spotify:album:38rprRSWLTehdqR0Kx50jj"
    }, 
    "artists": [
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/6ysKfYgiKUTMCuq2fSTLK3"
        }, 
        "href": "https://api.spotify.com/v1/artists/6ysKfYgiKUTMCuq2fSTLK3", 
        "id": "6ysKfYgiKUTMCuq2fSTLK3", 
        "name": "xander.", 
        "type": "artist", 
        "uri": "spotify:artist:6ysKfYgiKUTMCuq2fSTLK3"
      }, 
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/3xJD9x3Dw6g4g5naFYe0qi"
        }, 
        "href": "https://api.spotify.com/v1/artists/3xJD9x3Dw6g4g5naFYe0qi", 
        "id": "3xJD9x3Dw6g4g5naFYe0qi", 
        "name": "Philip Somber", 
        "type": "artist", 
        "uri": "spotify:artist:3xJD9x3Dw6g4g5naFYe0qi"
      }
    ], 
    "available_markets": [
      "AD", 
      "AE", 
      ...
    ], 
    "disc_number": 1, 
    "duration_ms": 188800, 
    "explicit": false, 
    "external_ids": {
      "isrc": "GBLV62109091"
    }, 
    "external_urls": {
      "spotify": "https://open.spotify.com/track/3rBM9PdRWFlssxl8S9z8IK"
    }, 
    "href": "https://api.spotify.com/v1/tracks/3rBM9PdRWFlssxl8S9z8IK", 
    "id": "3rBM9PdRWFlssxl8S9z8IK", 
    "is_local": false, 
    "name": "Tree House", 
    "popularity": 48, 
    "preview_url": "https://p.scdn.co/mp3-preview/1f8dbba682b29f1272d0a1a8c03feb8bdb7bc1f9?cid=d0241d33ae9f4e79a374ca4109b71f12", 
    "track_number": 10, 
    "type": "track", 
    "uri": "spotify:track:3rBM9PdRWFlssxl8S9z8IK"
  }, 
  "progress_ms": 105387, 
  "repeat_state": "context", 
  "shuffle_state": false, 
  "timestamp": 1642791044229
}
```