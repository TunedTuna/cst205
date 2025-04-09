from flask import Flask, render_template, flash, redirect
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'csumb-otter'
bootstrap = Bootstrap5(app)

class Playlist(FlaskForm):
    song_title = StringField(
        'Song Title', 
        validators=[DataRequired()]
    )
    artist_name =StringField(
        "Artist Name",
        validators=[DataRequired()]
    )

playlist = []

def store_song(my_song,my_artist):
    playlist.append(dict(
        song = my_song,
        date = datetime.today(),
        artist= my_artist,
    ))

@app.route('/', methods=('GET', 'POST'))
def index():
    form = Playlist()
    if form.validate_on_submit():
        store_song(form.song_title.data,form.artist_name.data)
        return redirect('/view_playlist')
    return render_template('index.html', form=form)


@app.route('/view_playlist')
def vp():
    return render_template('vp.html', playlist=playlist)

