

def get_new_releases(spotify, max_pages=100):
    all_releases = []
    current_page = 0
    releases = spotify.new_releases(limit=50)['albums']

    while releases and current_page < max_pages:
        release_items = releases['items']
        for release in release_items:
            release_info = release['release_date']
            all_releases.append(release_info)
        current_page += 1
        if releases['next']:
            releases = spotify.next(releases)['albums']
    return all_releases