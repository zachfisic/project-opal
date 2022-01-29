import spotipy as sp
from flask import current_app, render_template, url_for, redirect, flash
from flask_login import current_user, login_required, login_user, logout_user
from flaskapp import db
from flaskapp.models.user import User
from flaskapp.components.auth.func import session_cache_path, set_session_id
from flaskapp.components.main import main
from flaskapp.components.main.forms import LoginForm, RegistrationForm



@main.route('/')
def index():
    """Index route for the application.

    Displays welcome page, with additional information if user has authorized the application to use Spotify data.

    Returns:
        an HTML template
    """
    # set_session_id()
    # cache_handler = sp.cache_handler.CacheFileHandler(cache_path=session_cache_path())
    # auth_manager = sp.oauth2.SpotifyOAuth(scope=current_app.config['SPOTIPY_SCOPES_READ_ALL'] ,cache_handler=cache_handler, show_dialog=True)
    
    # # if access token doesn't exist or is invalid, return a generic template with the authorization URL
    # if not auth_manager.validate_token(cache_handler.get_cached_token()):
    #     auth_url = auth_manager.get_authorize_url()
    #     return render_template('welcome.html', auth_url=auth_url)
    
    # # The user has authorized the application, we can generate a Spotify instance with the configured authorization manager
    # spotify = sp.Spotify(auth_manager=auth_manager)
    # user = {
    #     'username': spotify.me()["display_name"]
    # }
    # artists = spotify.current_user_followed_artists(limit=20, after=None)['artists']['items']
    # return render_template('user.html', user=user, artists=artists)
    if current_user.is_authenticated:
        return redirect(url_for('user.index'))
    return render_template('main/welcome.html')



@main.route('/login', methods=['GET','POST'])
def login():
    # redirect already logged-in users back to the index
    if current_user.is_authenticated:
        return redirect(url_for('user.index'))

    form = LoginForm()
    if form.validate_on_submit():
        # form is valid, query for the user
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
        # User found, login and redirect back to index
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('user.index'))
    # Else render the normal login template
    return render_template('main/login.html', title='Sign In', form=form)


@main.route('/register', methods=['GET','POST'])
def register():
    # redirect already logged-in users back to the index
    if current_user.is_authenticated:
        return redirect(url_for('user.index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('User registered.')
        return redirect(url_for('main.login'))
    else:
        print('no')
    return render_template('main/register.html', title='Register', form=form)


@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))