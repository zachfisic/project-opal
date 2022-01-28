from flask import render_template, flash, redirect, url_for
from flaskapp.components.spotify.discover import discover
from flaskapp.components.spotify.discover.forms import ArtistForm
from flaskapp.components.auth.func import use_client_credentials


@discover.route('/', methods=['GET','POST'])
def index():
    form = ArtistForm()
    if form.validate_on_submit():
        id = form.artist_id.data
        print(id)
        # flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('spotify.discover.artist', artist_id=id))
    else:
        print('no')
    return render_template('artist_form.html', form=form)


@discover.route('/<artist_id>')
@use_client_credentials
def artist(spotify, artist_id):
    try:
        artist = spotify.artist(artist_id)
        related_artists = spotify.artist_related_artists(artist_id)['artists']
        return render_template('artist/artist_info.html', artist=artist, related_artists=related_artists)
    except Exception as e:
        print(e)
        return 'error'