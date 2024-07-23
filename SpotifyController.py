import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables from .env file
load_dotenv()

# Spotify API credentials
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
redirect_uri = os.getenv('REDIRECT_URL')

# Scope for accessing the user's playback state
scope = 'user-read-playback-state user-modify-playback-state'

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

def toggle_play_pause():
    current_track = sp.current_playback()
    if current_track is not None:
        if current_track['is_playing']:
            sp.pause_playback()
            print("Paused playback.")
        else:
            sp.start_playback()
            print("Resumed playback.")
    else:
        print("No track is currently playing.")

def skip_track():
    sp.next_track()
    print("Skipped to the next track.")

def go_back_track():
    sp.previous_track()
    print("Returned to the previous track.")

def show_current_track():
    current_track = sp.current_playback()
    if current_track is not None and current_track['item'] is not None:
        track_name = current_track['item']['name']
        artists = ", ".join([artist['name'] for artist in current_track['item']['artists']])
        print(f"Currently playing: {track_name} by {artists}")
    else:
        print("No track is currently playing.")

def show_current_playlist():
    current_track = sp.current_playback()
    if current_track is not None and current_track['context'] is not None:
        if current_track['context']['type'] == 'playlist':
            playlist_id = current_track['context']['uri'].split(':')[-1]
            playlist = sp.playlist(playlist_id)
            print(f"Currently listening to playlist: {playlist['name']}")
            print("Tracklist:")
            for i, item in enumerate(playlist['tracks']['items'], 1):
                track_name = item['track']['name']
                artists = ", ".join([artist['name'] for artist in item['track']['artists']])
                print(f"{i}. {track_name} by {artists}")
        else:
            print("Currently not listening to a playlist.")
    else:
        print("No track is currently playing.")

def play_song(song_name):
    search_results = sp.search(q=song_name, limit=1, type='track')
    if search_results['tracks']['items']:
        # Filter out karaoke versions or covers by selecting the most popular track
        tracks = search_results['tracks']['items']
        tracks.sort(key=lambda x: x['popularity'], reverse=True)  # Sort by popularity
        track_uri = tracks[0]['uri']  # Select the most popular track
        sp.start_playback(uris=[track_uri])
        print(f"Started playing: {tracks[0]['name']} by {', '.join([artist['name'] for artist in tracks[0]['artists']])}")
    else:
        print(f"No results found for the song: {song_name}")

def main():
    while True:
        # Display menu options
        print("\nSpotify CLI Menu:")
        print("*************************** Spotify Player Options ***************************")
        print(" ")
        print("1. Toggle Play/Pause")
        print("2. Skip Track")
        print("3. Go Back to Previous Track")
        print("")
        print("*************************** Display Options **********************************")
        print("")
        print("4. Show Current Playing Song")
        print("5. Show Current Playlist and Tracklist")
        print("")
        print("*************************** Search for a Song ********************************")
        print("")
        print("6. Play a Specific Song")
        print("7. Exit")

        # Get user input
        choice = input("Enter your choice: ")

        if choice == "1":
            toggle_play_pause()
        elif choice == "2":
            skip_track()
        elif choice == "3":
            go_back_track()
        elif choice == "4":
            show_current_track()
        elif choice == "5":
            show_current_playlist()
        elif choice == "6":
            song_name = input("Enter the name of the song: ")
            play_song(song_name)
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
