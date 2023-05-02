from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pprint


client_id = "e6b4ac23b33c4f399d979c3a613ec17d"
client_secret = "52bd4fd6461648b2b267147f01126132"

# lz_uri = 'spotify:artist:2DaxqgrOhkeH0fpeiQq2f4' # Oasis
# lz_uri = 'spotify:artist:0MK8l3nURwwQIjafvXoJJt' # AKG
lz_uri = 'spotify:artist:529ZdRwFoSKtQ0LPwKxGiu' # 장범준
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.artist_top_tracks(lz_uri)

# get top 10 tracks
for track in results['tracks'][:20]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print('genre: ' + track['genre'])