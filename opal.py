from flaskapp import create_app, db
from flaskapp.models.user import User

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}

if __name__ == '__main__':
    app.run(port=5000)