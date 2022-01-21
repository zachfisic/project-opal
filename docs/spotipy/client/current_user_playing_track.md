# current_user_playing_track()

Get information about the current users currently playing track.

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
            "spotify": "https://open.spotify.com/artist/0vg08N1z9G9LrGLkG1nNDS"
          }, 
          "href": "https://api.spotify.com/v1/artists/0vg08N1z9G9LrGLkG1nNDS", 
          "id": "0vg08N1z9G9LrGLkG1nNDS", 
          "name": "Mujo", 
          "type": "artist", 
          "uri": "spotify:artist:0vg08N1z9G9LrGLkG1nNDS"
        }, 
        {
          "external_urls": {
            "spotify": "https://open.spotify.com/artist/0CF9CnQbK6uS8u78KVnIPv"
          }, 
          "href": "https://api.spotify.com/v1/artists/0CF9CnQbK6uS8u78KVnIPv", 
          "id": "0CF9CnQbK6uS8u78KVnIPv", 
          "name": "Sweet Medicine", 
          "type": "artist", 
          "uri": "spotify:artist:0CF9CnQbK6uS8u78KVnIPv"
        }
      ], 
      "available_markets": [
        "AD", 
        "AE",
        ...
      ], 
      "external_urls": {
        "spotify": "https://open.spotify.com/album/1A0S991MrpSULZTOKiHTWp"
      }, 
      "href": "https://api.spotify.com/v1/albums/1A0S991MrpSULZTOKiHTWp", 
      "id": "1A0S991MrpSULZTOKiHTWp", 
      "images": [
        {
          "height": 640, 
          "url": "https://i.scdn.co/image/ab67616d0000b2734bc2fe61a610dea82c38851c", 
          "width": 640
        }, 
        {
          "height": 300, 
          "url": "https://i.scdn.co/image/ab67616d00001e024bc2fe61a610dea82c38851c", 
          "width": 300
        }, 
        {
          "height": 64, 
          "url": "https://i.scdn.co/image/ab67616d000048514bc2fe61a610dea82c38851c", 
          "width": 64
        }
      ], 
      "name": "Better Days", 
      "release_date": "2021-08-30", 
      "release_date_precision": "day", 
      "total_tracks": 8, 
      "type": "album", 
      "uri": "spotify:album:1A0S991MrpSULZTOKiHTWp"
    }, 
    "artists": [
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/0vg08N1z9G9LrGLkG1nNDS"
        }, 
        "href": "https://api.spotify.com/v1/artists/0vg08N1z9G9LrGLkG1nNDS", 
        "id": "0vg08N1z9G9LrGLkG1nNDS", 
        "name": "Mujo", 
        "type": "artist", 
        "uri": "spotify:artist:0vg08N1z9G9LrGLkG1nNDS"
      }, 
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/0CF9CnQbK6uS8u78KVnIPv"
        }, 
        "href": "https://api.spotify.com/v1/artists/0CF9CnQbK6uS8u78KVnIPv", 
        "id": "0CF9CnQbK6uS8u78KVnIPv", 
        "name": "Sweet Medicine", 
        "type": "artist", 
        "uri": "spotify:artist:0CF9CnQbK6uS8u78KVnIPv"
      }, 
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/0djvqMepj2XkHfvWTqkH1N"
        }, 
        "href": "https://api.spotify.com/v1/artists/0djvqMepj2XkHfvWTqkH1N", 
        "id": "0djvqMepj2XkHfvWTqkH1N", 
        "name": "G Mills", 
        "type": "artist", 
        "uri": "spotify:artist:0djvqMepj2XkHfvWTqkH1N"
      }
    ], 
    "available_markets": [
      "AD", 
      "AE",
      ...
    ], 
    "disc_number": 1, 
    "duration_ms": 123955, 
    "explicit": false, 
    "external_ids": {
      "isrc": "GBKQU2191184"
    }, 
    "external_urls": {
      "spotify": "https://open.spotify.com/track/11R5whlLhd99zoSCVTTpXT"
    }, 
    "href": "https://api.spotify.com/v1/tracks/11R5whlLhd99zoSCVTTpXT", 
    "id": "11R5whlLhd99zoSCVTTpXT", 
    "is_local": false, 
    "name": "Evergreen", 
    "popularity": 49, 
    "preview_url": "https://p.scdn.co/mp3-preview/235b3bb9a071f95d9776d746147df6fc4cc2d324?cid=d0241d33ae9f4e79a374ca4109b71f12", 
    "track_number": 5, 
    "type": "track", 
    "uri": "spotify:track:11R5whlLhd99zoSCVTTpXT"
  }, 
  "progress_ms": 27362, 
  "timestamp": 1642791233102
}
```