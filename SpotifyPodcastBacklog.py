# 1. Read secrect.json
# 2. Access Spotify account
# 3. Get list of subscribed podcasts
# 4. Add to playlist or create a new playlist

import json
import spotipy

class podcast_show:
    podcast_id = "1234"
    total_episodes = "1234"
    episode_name = []
    episode_ids = []

# Define podcast show
podcast = podcast_show()

ID = "123"
SECRET = "123"
username = "name"
scope = "user-library-read user-read-playback-position playlist-modify-public playlist-modify-private"

def read_secret():
    with open('secret.json') as json_file:
        data = json.load(json_file)
        c_ID = data['client_id']
        c_SECRET = data['client_secret']
        c_username = data['username']

    return c_ID, c_SECRET, c_username

def spotify_authentication():
    token = spotipy.util.prompt_for_user_token(username, scope, client_id=ID,client_secret=SECRET,redirect_uri='https://developer.spotify.com/dashboard/applications/8d942323bbf04dbfa2ab234d777f5200')

    sp = spotipy.Spotify(auth=token)

    return sp

def get_podcasts(sp):
    show_list = sp.current_user_saved_shows()

    sp_show_name = []
    sp_show_id = []

    for show in show_list['items']:
        sp_show_name.append(show['show']['name'])
        sp_show_id.append(show['show']['id'])
    
    # Select the podcast
    i = 0
    for i in range(len(sp_show_name)):
        print (str(i) + " - " + sp_show_name[i])
    
    select_list = input("Select the Podcast to use: ")

    # Get the podcast ID
    podcast.podcast_id = sp_show_id[int(select_list)]
    
    # Get the total number of episodes
    result = sp.show(podcast.podcast_id)
    podcast.total_episodes = result['total_episodes']

    return

def get_episodes(sp):
    # Get a list of subscibed podcasts
    get_podcasts(sp)

    episode_offset = 0

    #print("Total Episodes: " + str(podcast.total_episodes))

    # Get list of episodes
    if podcast.total_episodes < 50:
        episodes = sp.show_episodes(podcast.podcast_id)

        for episode in episodes['items']:
            podcast.episode_ids.append(episode['uri'])

    else:
        while episode_offset < podcast.total_episodes:
            episodes = sp.show_episodes(podcast.podcast_id, offset=episode_offset)

            for episode in episodes['items']:
                podcast.episode_ids.append(episode['uri'])

            episode_offset = episode_offset + 50
            #print ("Current offset: " + episode_offset)

    return

def add_backlog(sp):
    # Create a new playlist
    result = sp.user_playlist_create(username, "Podcast Backlog")
    playlist_id = result['id']

    #episode_list.reverse()

    offset = 0

    if podcast.total_episodes < 50:
        sp.playlist_add_items(playlist_id, podcast.episode_ids)
    else:
        while offset < podcast.total_episodes:
            sp.playlist_add_items(playlist_id, podcast.episode_ids[offset:offset+50])
            offset = offset + 50
    return

if __name__ == '__main__':
    json_secret = read_secret()
    ID = json_secret[0]
    SECRET = json_secret[1]
    username = json_secret[2]

    # Authenticte with Spotify
    sp = spotify_authentication()

    # Get a episodes in from choosen podcast
    get_episodes(sp)

    # Add backlog episodes to playlist
    add_backlog(sp)
