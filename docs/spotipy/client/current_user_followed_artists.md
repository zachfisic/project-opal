# current_user_followed_artists(limit=20, after=None)

Gets a list of the artists followed by the current authorized user

## Parameters
* `limit` - the number of entities to return
* `after` -  the last artist ID retrieved from the previous request

## Sample Response
```
{
  "artists": {
    "cursors": {
      "after": "5CkVLGKUJkIc1pmSk10QP4"
    }, 
    "href": "https://api.spotify.com/v1/me/following?type=artist&limit=50", 
    "items": [
      {
        "external_urls": {
          "spotify": "https://open.spotify.com/artist/06H83NVSKFktt0x1opb3OD"
        }, 
        "followers": {
          "href": null, 
          "total": 14231
        }, 
        "genres": [
          "float house"
        ], 
        "href": "https://api.spotify.com/v1/artists/06H83NVSKFktt0x1opb3OD", 
        "id": "06H83NVSKFktt0x1opb3OD", 
        "images": [
          {
            "height": 640, 
            "url": "https://i.scdn.co/image/ab6761610000e5ebcfdb4418e001300d8cefe911", 
            "width": 640
          }, 
          {
            "height": 320, 
            "url": "https://i.scdn.co/image/ab67616100005174cfdb4418e001300d8cefe911", 
            "width": 320
          }, 
          {
            "height": 160, 
            "url": "https://i.scdn.co/image/ab6761610000f178cfdb4418e001300d8cefe911", 
            "width": 160
          }
        ], 
        "name": "Matthieu Faubourg", 
        "popularity": 33, 
        "type": "artist", 
        "uri": "spotify:artist:06H83NVSKFktt0x1opb3OD"
      },
      ...
    ], 
    "limit": 50, 
    "next": "https://api.spotify.com/v1/me/following?type=artist&after=5CkVLGKUJkIc1pmSk10QP4&limit=50", 
    "total": 76
  }
}
```