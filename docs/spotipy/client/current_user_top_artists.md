# current_user_top_artists(limit=20, offset=0, time_range='medium_term')

Get the current user’s top artists

## Parameters
* `limit` - the number of entities to return
* `offset` - the index of the first entity to return
* `time_range` - Over what time frame are the affinities computed ("short_term", "medium_term", "long_term")

## Sample Response
```
{
  "href": "https://api.spotify.com/v1/me/top/artists?limit=50&offset=0&time_range=short_term", 
  "items": [
    {
      "external_urls": {
        "spotify": "https://open.spotify.com/artist/6eU0jV2eEZ8XTM7EmlguK6"
      }, 
      "followers": {
        "href": null, 
        "total": 617540
      }, 
      "genres": [
        "retro soul"
      ], 
      "href": "https://api.spotify.com/v1/artists/6eU0jV2eEZ8XTM7EmlguK6", 
      "id": "6eU0jV2eEZ8XTM7EmlguK6", 
      "images": [
        {
          "height": 640, 
          "url": "https://i.scdn.co/image/ab6761610000e5eb026d3ed0a2800958c1d59f4f", 
          "width": 640
        }, 
        {
          "height": 320, 
          "url": "https://i.scdn.co/image/ab67616100005174026d3ed0a2800958c1d59f4f", 
          "width": 320
        }, 
        {
          "height": 160, 
          "url": "https://i.scdn.co/image/ab6761610000f178026d3ed0a2800958c1d59f4f", 
          "width": 160
        }
      ], 
      "name": "Black Pumas", 
      "popularity": 64, 
      "type": "artist", 
      "uri": "spotify:artist:6eU0jV2eEZ8XTM7EmlguK6"
    }, 
    ...
}
```