import os
from flask import render_template, session, redirect, url_for
from flask_login import login_required
from flaskapp.components.auth.func import session_cache_path
from flaskapp.components.user import user


@user.route('/sign_out')
def sign_out():
    """Sign the current authorized user out of the application.
    
    Clears the user's session and returns them to the index route of the application.

    Returns:
        A redirect to the index route.
    """
    try:
        # Remove the cache file so that a new user can authorize.
        os.remove(session_cache_path())
        session.clear()
    except OSError as e:
        print(f"Error: {e.filename} - {e.strerror}.")
    return redirect(url_for('main.index'))


@user.route('/')
@login_required
def index():
    return render_template('user/home.html')



