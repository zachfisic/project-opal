from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# 6nS5roXSAGhTGr34W6n7Et

class ArtistForm(FlaskForm):
    artist_id = StringField('Artist ID', validators=[DataRequired()])
    submit = SubmitField('Find')