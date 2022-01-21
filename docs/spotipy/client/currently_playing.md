# currently_playing(market=None, additional_types=None)

Get user’s currently playing track.

## Parameters:
- market - an ISO 3166-1 alpha-2 country code.
- additional_types - episode to get podcast track information

## Sample Response
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
  "is_playing": true, 
  "item": {
    "album": {
      "album_type": "album", 
      "artists": [
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/1SzLvjYm0lQLPi3AneCpDO"
          }, 
          "href": "https://api.spotify.com/v1/artists/1SzLvjYm0lQLPi3AneCpDO", 
          "id": "1SzLvjYm0lQLPi3AneCpDO", 
          "name": "Kurt Stewart", 
          "type": "artist", 
          "uri": "spotify:artist:1SzLvjYm0lQLPi3AneCpDO"
        }, 
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/2UxHowdAHxVWPhQQswzpT6"
          }, 
          "href": "https://api.spotify.com/v1/artists/2UxHowdAHxVWPhQQswzpT6", 
          "id": "2UxHowdAHxVWPhQQswzpT6", 
          "name": "Lomme", 
          "type": "artist", 
          "uri": "spotify:artist:2UxHowdAHxVWPhQQswzpT6"
        }
      ], 
      "available_markets": [
        "AD", 
        "AE",
        ...
      ], 
      "external_urls": {
        "spotify": "https://open.spotify.com/album/1qT0jx1jNSzgWzvOt50qfI"
      }, 
      "href": "https://api.spotify.com/v1/albums/1qT0jx1jNSzgWzvOt50qfI", 
      "id": "1qT0jx1jNSzgWzvOt50qfI", 
      "images": [
        {
          "height": 640, 
          "url": "https://i.scdn.co/image/ab67616d0000b273879c54e8306d919409d1a548", 
          "width": 640
        }, 
        {
          "height": 300, 
          "url": "https://i.scdn.co/image/ab67616d00001e02879c54e8306d919409d1a548", 
          "width": 300
        }, 
        {
          "height": 64, 
          "url": "https://i.scdn.co/image/ab67616d00004851879c54e8306d919409d1a548", 
          "width": 64
        }
      ], 
      "name": "Pegan Hill", 
      "release_date": "2021-04-28", 
      "release_date_precision": "day", 
      "total_tracks": 11, 
      "type": "album", 
      "uri": "spotify:album:1qT0jx1jNSzgWzvOt50qfI"
    }, 
    "artists": [
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/1SzLvjYm0lQLPi3AneCpDO"
        }, 
        "href": "https://api.spotify.com/v1/artists/1SzLvjYm0lQLPi3AneCpDO", 
        "id": "1SzLvjYm0lQLPi3AneCpDO", 
        "name": "Kurt Stewart", 
        "type": "artist", 
        "uri": "spotify:artist:1SzLvjYm0lQLPi3AneCpDO"
      }, 
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/2UxHowdAHxVWPhQQswzpT6"
        }, 
        "href": "https://api.spotify.com/v1/artists/2UxHowdAHxVWPhQQswzpT6", 
        "id": "2UxHowdAHxVWPhQQswzpT6", 
        "name": "Lomme", 
        "type": "artist", 
        "uri": "spotify:artist:2UxHowdAHxVWPhQQswzpT6"
      }
    ], 
    "available_markets": [
      "AD", 
      "AE",
      ...
    ], 
    "disc_number": 1, 
    "duration_ms": 150050, 
    "explicit": false, 
    "external_ids": {
      "isrc": "GBKQU2145610"
    }, 
    "external_urls": {
      "spotify": "https://open.spotify.com/track/5JYVocZpeUBB12ZzuxscsQ"
    }, 
    "href": "https://api.spotify.com/v1/tracks/5JYVocZpeUBB12ZzuxscsQ", 
    "id": "5JYVocZpeUBB12ZzuxscsQ", 
    "is_local": false, 
    "name": "Window Seat", 
    "popularity": 55, 
    "preview_url": "https://p.scdn.co/mp3-preview/1de02e6fc9455788f334a2835c868b03c478d7fb?cid=d0241d33ae9f4e79a374ca4109b71f12", 
    "track_number": 5, 
    "type": "track", 
    "uri": "spotify:track:5JYVocZpeUBB12ZzuxscsQ"
  }, 
  "progress_ms": 133591, 
  "timestamp": 1642790750561
}
```