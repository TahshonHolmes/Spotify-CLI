# Spotify CLI Application

This Python script provides a command-line interface (CLI) for interacting with Spotify using the Spotipy library. The CLI allows users to control playback, view current track and playlist information, and search for and play specific songs.

## Features

- **Toggle Play/Pause:** Start or pause the current playback.
- **Skip Track:** Skip to the next track in the current playlist.
- **Go Back to Previous Track:** Return to the previous track in the current playlist.
- **Show Current Playing Song:** Display information about the currently playing song.
- **Show Current Playlist and Tracklist:** Display the current playlist and its tracklist.
- **Play a Specific Song:** Search for and play a specific song by name.

## Requirements

- Python 3.x
- Spotipy library
- A Spotify developer account with API credentials

## Setup

1. **Install Spotipy:**

   ```bash
   pip install spotipy

2. **Create a .env file:** 
    Add your Spotify API credentials to a .env file in the same directory as the script. The .env file should contain the following variables:

    ```makefile
    CLIENT_ID=your_spotify_client_id
    CLIENT_SECRET=your_spotify_client_secret
    REDIRECT_URL=your_spotify_redirect_uri

## Usage 
Run the script using Python: 


    python SpotifyController.py