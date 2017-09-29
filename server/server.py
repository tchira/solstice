from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

SPOTIPY_CLIENT_ID = '151f5ceb8b834c839bdec45b6d451c62'
SPOTIPY_CLIENT_SECRET = '6f53990491224119976244d5e77a5847'

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


@app.route("/artist")
@cross_origin()
def get_artist_by_name():
    artist_name = request.args.get('name')
    artist_results = spotify.search(q='artist:' + artist_name, type='artist')
    artist = artist_results.get('artists').get('items')[0]
    return jsonify(artist)


@app.route("/related")
def related_artists():
    artist_id = request.args.get('id')
    related = spotify.artist_related_artists(artist_id)
    return jsonify(related)


app.run(port=5000)
